from led import RGBdata, Neopixel
import os
leds = Neopixel(3)
leds.fill(255,255,255,100)
print(leds.colors()) 
leds.pixels[2]((0,0,0,100))
print(leds.colors())      
buf = bytes(leds.ws2812_Data())
print(buf)


