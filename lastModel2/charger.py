# 차저
# flash: mat blue 점점밝게, stop: red 점점밝게
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
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'flash2':
        red = 0
        green = 0
        blue = 0
        
        #점점 밝게
        for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (0, num, 0)
                    np.show()
    
    if incoming == 'stop2':
        red = 0
        green = 0
        blue = 0
        
        #점점 밝게
        for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (0, 199-num, 0)
                    np.show()
                    
    if incoming == 'run2':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

    if incoming == 'flow2':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

    if incoming == 'auth2':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

    if incoming == 'close2':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
