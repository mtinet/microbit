# 조종기 remoteRunFlash
import radio
from random import randint
from microbit import *
import neopixel

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()
np = neopixel.NeoPixel(pin0, 16)

# Event loop.
while True:
    if button_a.was_pressed():
        radio.send('run')  # a-ha
    
    if button_b.was_pressed():
        radio.send('flash')  # a-ha
