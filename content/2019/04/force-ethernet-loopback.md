Title: Forcing ethernet traffic onto physical interfaces
Date: 2020-04-28
Slug: force-ethernet-loopback

When you're working with a device that has two ethernet ports, it can be sometimes useful for hardware benchmarking or testing purposes to do a loopback test where one port connects directly to the other.

![ethernet loopback](/images/ethernetloopback.png)

By default, and somewhat annoyingly, Linux is smart about routing traffic between ethernet adapters on the same system, leading to results from iperf like this:

```
:::bash
[ ID] Interval           Transfer     Bitrate         Retr
[  5]   0.00-10.00  sec  3.70 GBytes  3.18 Gbits/sec    0             sender
[  5]   0.00-10.04  sec  3.70 GBytes  3.16 Gbits/sec                  receiver
```

Which is impressive, but obviously means that no data is being put out  through the physical interface.

Luckily [network namespaces](https://en.wikipedia.org/wiki/Linux_namespaces#Network_(net)) can be used to force traffic out across the physical medium. By placing each adapter into its own namespace, the namespaces can't see each other and so the traffic is forced out on the wire.

To do this:

1. Create a namespace for each adapter
```
:::bash
ip netns add ns_eth0
ip netns add ns_eth1
```
2. Move the adapters into the namespaces
```
:::bash
ip netns set eth0 ns ns_eth0
ip netns set eth1 ns ns_eth1
```
3. Assign ip addresses to each adapter
```
:::bash
ip netns exec ns_eth0 ip addr add dev eth0 192.168.1.1/24
ip netns exec ns_eth1 ip addr add dev eth1 192.168.1.2/24
```
4. Bring the adapters up
```
:::bash
ip netns exec ns_eth0 ip link set eth0 up
ip netns exec ns_eth1 ip link set eth1 up
```
5. Check that each adapter can ping the other
```
:::bash
ip netns exec ns_eth0 ping 192.168.1.2
ip netns exec ns_eth1 ping 192.168.1.1
```
6. Run your tests, happy in the knowledge that the traffic is really going out on the physical interface!
```
:::bash
ip netns exec ns_eth0 iperf3 -s
ip netns exec ns_eth1 iperf3 -c 192.168.1.1
```
