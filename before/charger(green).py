# 차저
# flash: green 점점 밝게, stop: red 점점밝게
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
    if incoming == 'flash':
        red = 0
        green = 0
        blue = 0
        
        #점점 밝게
        for num in range(0, 255):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (0, num, 0)
                    np.show()
    
    if incoming == 'stop':
        red = 0
        green = 0
        blue = 0
        
        #점점 밝게
        for num in range(0, 200):
                for pixel_id in range(0, len(np)):
                    np[pixel_id] = (0, 199-num, 0)
                    np.show()
  
