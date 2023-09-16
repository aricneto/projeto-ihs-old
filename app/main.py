#!/usr/bin/python3

import os, sys
from fcntl import ioctl
from time import sleep

# ioctl commands defined at the pci driver
RD_SWITCHES   = 24929
RD_PBUTTONS   = 24930
WR_L_DISPLAY  = 24931
WR_R_DISPLAY  = 24932
WR_RED_LEDS   = 24933
WR_GREEN_LEDS = 24934

def main():
    if len(sys.argv) < 2:
        print("Error: expected more command line arguments")
        print("Syntax: %s </dev/device_file>"%sys.argv[0])
        exit(1)

    global fd
    fd = os.open(sys.argv[1], os.O_RDWR)

    #wait until fd is loaded
    print("loading")
    sleep(3)
    print("loaded\n\n")

    # data to write
    data = 0x40404079;

    #liga_led(0b101010101010101010, WR_RED_LEDS)
    #liga_led(0b101010101, WR_GREEN_LEDS)
    
    #sleep(2)
    for i in range(2):
        #liga_led(0b1001111010011110, WR_R_DISPLAY)
        liga_led(0b010001100100000010000001101000000, WR_R_DISPLAY)

    
#    with os.fdopen(os.open(sys.argv[1], os.O_RDWR), "w") as fdd:
#        ioctl(fdd, RD_SWITCHES)
#        k = os.read(fdd, 4)
#        n = int.from_bytes(red, 'little')
#        print(f"{n:016b}")
    #for i in range(0, 5):
        #data = i

        #sw = le_switch()
        #b = le_botao()
        #liga_led(i, WR_R_DISPLAY)
        #liga_led(sw, WR_RED_LEDS)
        #sleep(1)
        #liga_led(b, WR_GREEN_LEDS)
        #sleep(1)
	#liga_led(b, WR_L_DISPLAY)
        #liga_led(b, WR_R_DISPLAY)
        #sleep(0.005) 

    print("botao")

    while True:
        b = le_botao()
        sw = le_switch()
        liga_led(b, WR_GREEN_LEDS)
        liga_led(sw, WR_RED_LEDS)
        liga_led(sw, WR_R_DISPLAY)
        liga_led(sw, WR_L_DISPLAY)
        if b == 0b0101:
            break
    
    # for i in range(20):
    #     ioctl(fd, RD_PBUTTONS)
    #     red = os.read(fd, 4); # read 4 bytes and store in red var
    #     red = os.read(fd, 4); # read 4 bytes and store in red var
    #     n = int.from_bytes(red, 'little')
    #     print(f"button {n:04b}")
    #     sleep(0.5)

    

    os.close(fd)

def le_switch():
    sleep(0.1)
    ioctl(fd, RD_SWITCHES)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    red = os.read(fd, 4); # read 4 bytes and store in red var
    n = int.from_bytes(red, 'little')
    print(f"switch {n:016b}")
    return n

def le_botao():
    sleep(0.1)
    ioctl(fd, RD_PBUTTONS)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    red = os.read(fd, 4); # read 4 bytes and store in red var
    n = int.from_bytes(red, 'little')
    print(f"buttons {n:04b}")
    return n

def liga_led(leds, cor):
    if (cor not in [WR_RED_LEDS, WR_GREEN_LEDS, WR_L_DISPLAY, WR_R_DISPLAY]):
        print ("nao existe essa cor")
        return 0
    global fd
    ioctl(fd, cor)
    retval = os.write(fd, leds.to_bytes(4, 'little'))
    print(f"led ({cor}) [{retval}]: ({leds:018b})")

if __name__ == '__main__':
    main()
