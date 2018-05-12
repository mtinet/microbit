# 테일라이트  
# flow: red*2 - light red, stop: red - light red
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
    if incoming == 'run':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (50, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

    if incoming == 'flash':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            
    if incoming == 'flow':
        for i in range(0, 2):
            for pixel_id in range(0, len(np)-8):
                red = 255
                green = 0
                blue = 0
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)
                np[pixel_id+8] = (red, green, blue)
        
                # Display the current pixel data on the Neopixel strip
                np.show()
                sleep(50)
            for pixel_id in range(0, len(np)):
                red = 0
                green = 0
                blue = 0
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)
                
        
                # Display the current pixel data on the Neopixel strip
                np.show()
                sleep(50)
                
        for pixel_id in range(0, len(np)):
            red = 255
            green = 0
            blue = 0
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            sleep(50)
        sleep(1000)
        
        for pixel_id in range(0, len(np)):
                red = 50
                green = 0
                blue = 0
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)
        
            # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(50)
            
    if incoming == 'stop':
        for pixel_id in range(0, len(np)):
            red = 255
            green = 0
            blue = 0
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(2000)
        
        for pixel_id in range(0, len(np)):
                red = 50
                green = 0
                blue = 0
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)
        
            # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(50)
        
    if incoming == 'auth':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (255, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            
    if incoming == 'close':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()        
