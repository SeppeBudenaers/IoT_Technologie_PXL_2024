from led import RGBdata, Neopixel
import os
leds = Neopixel(3)
leds.fill(RGBdata(255,255,255,100))

print(leds.colors()) 

leds.set_pixel(2,RGBdata(255,0,255,10))

print(leds.colors())
