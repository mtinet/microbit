# 머리띠  
# flow: red*2 - light red, stop: red - light red
import radio
from random import randint
from microbit import *
import neopixel
 
# The radio won't work unless it's switched on.
radio.on()
np = neopixel.NeoPixel(pin0, 29)
 
# Event loop.
while True:
    for pixel_id in range(0, len(np)):
        red = 0
        green = 0
        blue = 0

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip
        np.show()

    incoming = radio.receive()
    if incoming == 'run':                
        for i in range(0, 3):
            for pixel_id in range(0, len(np)/2):
                red = 255
                green = 255
                blue = 255
       
                 # Assign the current LED a random red, green and blue value between 0 and 60
                np[14] = (red, green, blue)
                np[15+pixel_id-1] = (red, green, blue)
                np[13-pixel_id+1] = (red, green, blue)
        

                 # Display the current pixel data on the Neopixel strip
                np.show()
                sleep(50)
            for pixel_id in range(0, len(np)/2):
                red = 0
                green = 0
                blue = 0
         
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[14] = (red, green, blue)
                np[15+pixel_id-1] = (red, green, blue)
                np[13-pixel_id+1] = (red, green, blue)
        
    
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
        sleep(100)
        

    if incoming == 'flash':                
        for pixel_id in range(0, len(np)):

            np[pixel_id] = (0, 0, 0)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

    if incoming == 'flow':                
        for i in range(0, 2):
            for pixel_id in range(0, len(np)/2):
                red = 0
                green = 0
                blue = 255
       
                 # Assign the current LED a random red, green and blue value between 0 and 60
                np[14] = (red, green, blue)
                np[15+pixel_id-1] = (red, green, blue)
                np[13-pixel_id+1] = (red, green, blue)
        

                 # Display the current pixel data on the Neopixel strip
                np.show()
                sleep(50)
            for pixel_id in range(0, len(np)/2):
                red = 0
                green = 0
                blue = 0
         
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[14] = (red, green, blue)
                np[15+pixel_id-1] = (red, green, blue)
                np[13-pixel_id+1] = (red, green, blue)
        
    
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
        sleep(100)
        
        for pixel_id in range(0, len(np)):
                red = 0
                green = 0
                blue = 0
        
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
            for pixel_id in range(0, len(np)/2):
                red = 0
                green = 0
                blue = 255
       
                 # Assign the current LED a random red, green and blue value between 0 and 60
                np[14] = (red, green, blue)
                np[15+pixel_id-1] = (red, green, blue)
                np[13-pixel_id+1] = (red, green, blue)
        

                 # Display the current pixel data on the Neopixel strip
                np.show()
                sleep(50)
            for pixel_id in range(0, len(np)/2):
                red = 0
                green = 0
                blue = 0
         
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[14] = (red, green, blue)
                np[15+pixel_id-1] = (red, green, blue)
                np[13-pixel_id+1] = (red, green, blue)
        
    
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
        sleep(100)
        
        for pixel_id in range(0, len(np)):
                red = 0
                green = 0
                blue = 0
        
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)
       
            # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(50)
        
    if incoming == 'close':
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
                red = 0
                green = 0
                blue = 0

         
                # Assign the current LED a random red, green and blue value between 0 and 60
                np[pixel_id] = (red, green, blue)

         
            # Display the current pixel data on the Neopixel strip

        np.show()
        sleep(50)        
