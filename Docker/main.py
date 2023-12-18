import time
from neopixel import Neopixel
 
numpix = 1
pixels = Neopixel(numpix, 0, 2, "GRB")
 

green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
pixels.show()

 
while True:
    pixels.fill(red)
    pixels.show()
    time.sleep(1)
    pixels.fill(green)
    pixels.show()
    time.sleep(1)
    pixels.fill(blue)
    pixels.show()
    time.sleep(1)