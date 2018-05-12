# 사이드 인디케이터(새버전)  
# run: green, flash: red, flow: blue*2 - green
import radio
from random import randint
from microbit import *
import neopixel

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()
np = neopixel.NeoPixel(pin0, 4)

for pixel_id in range(0, len(np)):
    red = 0
    green = 200
    blue = 0

    # Assign the current LED a random red, green and blue value between 0 and 60
    np[pixel_id] = (red, green, blue)

    # Display the current pixel data on the Neopixel strip
    np.show()
        
# Event loop.
while True:
    incoming = radio.receive()
    if incoming == 'run2':
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 200, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            
    if incoming == 'flash2':
        for num in range(0, 200):
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (num, 0, 0)
    
            np.show()  
            
    if incoming == 'flow2':
        for num in range(0, 200):
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (0, num, 0)
    
            np.show()
            
    if incoming == 'stop2':
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 200, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()            

    if incoming == 'auth2':
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 200, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()          
            
    if incoming == 'close2':
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (200, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
