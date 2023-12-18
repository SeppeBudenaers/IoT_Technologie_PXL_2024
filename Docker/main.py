import time
from neopixel import Neopixel
 
numpix = 14
pixels = Neopixel(numpix, 0, 2, "GRB")
 

green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

 
while True:
    pixels.fill(red)
    time.sleep(1)
    pixels.fill(green)
    time.sleep(1)
    pixels.fill(blue)
    time.sleep(1)