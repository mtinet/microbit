# 조종기 remoteAuthClose
import radio
from random import randint
from microbit import *
import neopixel

flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

radio.on()
np = neopixel.NeoPixel(pin0, 16)

# Event loop.
while True:
    if button_a.was_pressed():
        radio.send('auth2')  # a-ha
    
    if button_b.was_pressed():
        radio.send('close2')  # a-ha
