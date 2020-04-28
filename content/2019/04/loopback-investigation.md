
```
root@raspberrypi4:~# iperf3 -s -B 10.0.0.1
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------
Accepted connection from 10.0.0.1, port 36372
[  5] local 10.0.0.1 port 5201 connected to 10.0.0.1 port 36374
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-1.00   sec   356 MBytes  2.99 Gbits/sec
[  5]   1.00-2.00   sec   370 MBytes  3.10 Gbits/sec
[  5]   2.00-3.00   sec   368 MBytes  3.09 Gbits/sec
[  5]   3.00-4.00   sec   368 MBytes  3.09 Gbits/sec
[  5]   4.00-5.00   sec   366 MBytes  3.07 Gbits/sec
[  5]   5.00-6.00   sec   367 MBytes  3.08 Gbits/sec
[  5]   6.00-7.00   sec   364 MBytes  3.05 Gbits/sec
[  5]   7.00-8.00   sec   366 MBytes  3.07 Gbits/sec
[  5]   8.00-9.00   sec   365 MBytes  3.06 Gbits/sec
[  5]   9.00-10.00  sec   368 MBytes  3.09 Gbits/sec
[  5]  10.00-10.03  sec  9.50 MBytes  3.02 Gbits/sec
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bitrate
[  5]   0.00-10.03  sec  3.58 GBytes  3.07 Gbits/sec                  receiver
```

How to send on the loopback adapter faster
