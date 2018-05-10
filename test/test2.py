# 흰색 줄무늬가 흐르게 하는 예제
from microbit import *
import neopixel 
from random import randint

np = neopixel.NeoPixel(pin0, 10);

while True:
    for pixel_id in range(0, 9):
        red = 255;
        green = 255;
        blue = 255;
        np.clear()
        # np[pixel_id-9] = (red-180, green-180, blue-180)
        # np[pixel_id-8] = (red-160, green-160, blue-160)
        # np[pixel_id-7] = (red-210, green-210, blue-210)
        # np[pixel_id-6] = (red-180, green-180, blue-180)
        # np[pixel_id-5] = (red-150, green-150, blue-150)
        # np[pixel_id-4] = (red-120, green-120, blue-120)
        np[pixel_id-3] = (red-90, green-90, blue-90)
        np[pixel_id-2] = (red-60, green-60, blue-60)
        np[pixel_id-1] = (red-30, green-30, blue-30)
        np[pixel_id] = (red, green, blue)
        np.show()
        sleep(50);
