# 차폭등
import radio
from random import randint
from microbit import *
import neopixel

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()
np = neopixel.NeoPixel(pin0, 4)

# Event loop.
while True:
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'run2':
        for num in range(0, 255):
            np[0] = (num, num, num)
            np[1] = (num, num, num)
            np[2] = (num, 0, 0)
            np[3] = (num, 0, 0)
            np.show()
            sleep(10)

    if incoming == 'flash2':
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np.show()
        sleep(10)    
            
    if incoming == 'flow2':
        for num in range(0, 255):
            np[0] = (num, num, num)
            np[1] = (num, num, num)
            np[2] = (num, 0, 0)
            np[3] = (num, 0, 0)
            np.show()
            sleep(10)
            
    if incoming == 'stop2':
        for num in range(0, 255):
            np[0] = (num, num, num)
            np[1] = (num, num, num)
            np[2] = (num, 0, 0)
            np[3] = (num, 0, 0)
            np.show()
            sleep(10)
            
    if incoming == 'auth2':
        for num in range(0, 255):
            np[0] = (num, num, num)
            np[1] = (num, num, num)
            np[2] = (num, 0, 0)
            np[3] = (num, 0, 0)
            np.show()
            sleep(10)
            
    if incoming == 'close2':                
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np.show()
        sleep(10) 
