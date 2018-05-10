# 사이드 인디케이터  
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

# Event loop.
while True:
    for pixel_id in range(0, len(np)):
        red = 0
        green = 50
        blue = 0

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip
        np.show()
        
    incoming = radio.receive()
    if incoming == 'run':
        for i in range(0, 5):
            for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (0, num, 0)
        
                np.show()

            
    if incoming == 'flash':
        for i in range(0, 5):
            for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (num, 0, 0)
            
                np.show()
                sleep(5)
            for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (199-num, 0, 0)
            
                np.show()
                sleep(5)

    if incoming == 'flow':
# 초록색이 켜지게 하려면 아래를 활성화할 것
        for i in range(0, 5):
            for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (0, num, 0)
        
                np.show()
# 파란색이 흘러가게 하려면 아래를 활성화할 것
#         for i in range(0, 2):
#             for pixel_id in range(0, len(np)):
#                 red = 0
#                 green = 0
#                 blue = 255
        
#                 # Assign the current LED a random red, green and blue value between 0 and 60
#                 np[pixel_id] = (red, green, blue)
        
#                 # Display the current pixel data on the Neopixel strip
#                 np.show()
#                 sleep(50)
#             for pixel_id in range(0, len(np)):
#                 red = 0
#                 green = 0
#                 blue = 0
        
#                 # Assign the current LED a random red, green and blue value between 0 and 60
#                 np[pixel_id] = (red, green, blue)
                
        
#                 # Display the current pixel data on the Neopixel strip
#                 np.show()
#                 sleep(50)
        
        for num in range(0, 200):   
            for pixel_id in range(0, len(np)):
                np[pixel_id] = (0, num, 0)
        
            np.show()
