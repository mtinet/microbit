# 헤드라이트
# 
import radio
from random import randint
from microbit import *
import neopixel

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()
np = neopixel.NeoPixel(pin0, 8)

# Event loop.
while True:
    incoming = radio.receive()
    if incoming == 'run':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (255, 255, 255)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

    if incoming == 'flash':
        red = 0
        green = 0
        blue = 0
        
        # 점점 밝게  
        for count in range(0, 3):
            for num in range(0, 150):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (num, num, num)
                    np.show()
        # 점점 어둡게  
            for num in range(0, 150):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (150-num, 150-num, 150-num)
                    np.show()
        
        for pixel_id in range(0, len(np)):
            red = 50
            green = 50
            blue = 50
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
        # Display the current pixel data on the Neopixel strip
        np.show()
                    
    if incoming == 'flow':
        for i in range(0, 2):
            for pixel_id in range(0, len(np)):
                red = 150
                green = 150
                blue = 150
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)

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
            green = 255
            blue = 255
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            sleep(50)
            
    if incoming == 'stop':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
           
    if incoming == 'auth':                
        for i in range(0, 2):
            for pixel_id in range(0, len(np)):
                red = 150
                green = 150
                blue = 150
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)

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
            green = 255
            blue = 255
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            sleep(50)
            
    if incoming == 'close':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()                
