import time
from machine import Pin

# D13 controls the tiny built-in LED on the Arduino itself
led_builtin = Pin("D13", Pin.OUT)

# D11 controls your external breadboard LED
led_external = Pin("D11", Pin.OUT)

while True:
    led_builtin.value(1)
    led_external.value(1)
    time.sleep(1)

    led_builtin.value(0)
    led_external.value(0)
    time.sleep(1)
