# !/usr/bin/env python3

# =================================================================================================
# USAGE: This script checks the availability of a specified URL(s) and blinks an LED if it's down.
# =================================================================================================

import os
from gpiozero import LED
from time import sleep

led = LED(25)
blink = 1
blink_max = 10
led_on_blink_timer=2
led_off_blink_timer=0.1
url="https://hariprasad.dev"

status_code = os.popen(f"curl -A \"gpiochecker\" -I -s -o /dev/null -w \"%{{http_code}}\" {url}").readlines()
print(f"Response status code {status_code}")

if int(status_code[0]) != 200:
    while blink < blink_max:
        print(f"Blink {blink}")
        led.on()
        sleep(led_on_blink_timer)
        led.off()
        sleep(led_off_blink_timer)
        blink=blink+1