# test3.py - 흰색 줄무늬가 흐르게 하는 예제  
from microbit import *
import neopixel 
from random import randint

np = neopixel.NeoPixel(pin0, 10);

while True:
    for pixel_id in range(0, 9):
        red = 255
        green = 255
        blue = 255
        brightness = 0
        np.clear()
        for pixel_brightness in range(0, 20) :
            brightness = brightness + 5       
            np[pixel_id-5] = (red-255, green-255, blue-255)
            np[pixel_id-4] = (red-brightness-40, green-brightness-40, blue-brightness-40)
            np[pixel_id-3] = (red-brightness-30, green-brightness-30, blue-brightness-30)
            np[pixel_id-2] = (red-brightness-20, green-brightness-20, blue-brightness-20)
            np[pixel_id-1] = (red-brightness-10, green-brightness-10, blue-brightness-10)
            np[pixel_id] = (red-brightness, green-brightness, blue-brightness)
            np.show()
            # sleep(10);
