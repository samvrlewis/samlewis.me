Title: MSP432 serial printf
Date: 2015-05-17
Slug: msp432-serial-printf

While the [MSP432](http://www.ti.com/lsds/ti/microcontrollers_16-bit_32-bit/msp/low_power_performance/msp432p4x/getting_started.page?paramCriteria=no), does seem to be an kickin' rad microcontroller, I've noticed a distinct lack of resources online to do the most basic microcontrolley stuff.

So this is a quick bit of code to get a serial/UART connection up and going from the MSP432 to your computer over the USB connection. Perfect for any debugging that you might want to do, or communication with other serial devices (for example the exciting ESP8266 which I'll cover in a later blog post).

The MSP432-printf library, which is largely from 43oh member OPossum ([printf for the MSP430](http://www.msp430launchpad.com/2012/06/using-printf.html)), lets you print to any serial module using standard printf syntax. For example: `printf(EUSCI_A0_MODULE, "String one: %d", 1)`. The code for the library can be [found on my GitHub](https://github.com/samvrlewis/MSP432-printf/blob/master/printf.c). 

An example of using this printf library with the MSP432 is shown below. 

<script src="http://gist-it.appspot.com/https://github.com/samvrlewis/MSP432-printf/blob/master/printf_example.c">
</script>

The code configures `EUSCI_A0_MODULE` to be used and then prints to it. `EUSCI_A0_MODULE` is, by default the application UART that you can connect to over USB from your PC. One thing to note is to make sure that `EUSCI_A_UART_LSB_FIRST` is set in the UART config, rather than `EUSCI_A_UART_MSB_FIRST`. [According to wikipedia](http://en.wikipedia.org/wiki/Serial_port), MSB first serial communication is rarely used and it's much more common to use little endian or LSB first communications. If you use a program like PuTTY, it's likely that it'll interpret the serial stream as little endian.

To connect to the MSP432, I use [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/). On my PC, the MSP432 is on COM1. It's possible to configure and use serial modules other than `EUSCI_A0_MODULE` but this may involve some [datasheet](http://www.ti.com/lit/ds/slas826a/slas826a.pdf) investigation!