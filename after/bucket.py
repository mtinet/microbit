# 버킷
# auth: white, close: off 3 secs later 
import radio
from random import randint
from microbit import *
import neopixel

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()
np = neopixel.NeoPixel(pin0, 47)

# Event loop.
while True:
    incoming = radio.receive()
    if incoming == 'auth':
        for num in range(0, 200):
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (num, num, num)
    
            np.show()

            
    if incoming == 'close':
        sleep(1000)
        for num in range(0, 200):   
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (199-num, 199-num, 199-num)
        
            np.show()
