# A버튼을 누르면 라디오를 통해 'flow'라는 문자열이 전달되고, 이를 받은 마이크로비트의 네오픽셀에서 흰색 줄무늬가 흐르게 하는 예제(라이트 8개)  
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
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send('flow')  # a-ha
    # Read any incoming messages.
    incoming = radio.receive()
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
            red = 150
            green = 150
            blue = 150
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            sleep(50)
