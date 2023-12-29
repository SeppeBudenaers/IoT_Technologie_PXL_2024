from led import RGBdata, Neopixel
# import wiringpi
import spidev
import argparse
import requests
import time
from time import sleep
import os

def GetAPIKEYOS():
    try:
        print(os.environ)
        API_KEY = os.environ.get('API_KEY')
        return API_KEY
    except KeyError:
        print("Environmental Key Does not exist")

def GetAPIKEYARG():
    parser = argparse.ArgumentParser(description='IOT program')
    parser.add_argument('API_KEY', metavar='API_KEY', type=str, help='enter your API key')
    args = parser.parse_args()
    return args.API_KEY

def GetAPIKEYFile(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# GPIO Init 
# ledPin = 5
# wiringpi.wiringPiSetup()
# wiringpi.pinMode(ledPin,1) 
#SPI / ws2812 init
spi = spidev.SpiDev()
spi.open(0,0) # open /dev/spidev0.0
spi.mode = 0b00
spi.max_speed_hz = 6250000

leds = Neopixel(1)

# Choose one of the methods to get API_KEY
# API_KEY = GetAPIKEYOS()
# print(API_KEY)
# API_KEY = GetAPIKEYARG()
# print(API_KEY)
# API_KEY = GetAPIKEYFile("secretfile.txt")
# print(API_KEY)

# url = 'http://iot.pxl.bjth.xyz'

# headers = {
#     '-h':"X-Api-Key: "+str(API_KEY)
# }

# main loop
try:  
    # for i in  range (0,10):
    #     data = {
    #         "id": time.time(),
    #         "value": 25.5,
    #         "scale": "F"
    #     }
    #     response = requests.put(url, json=data, headers=headers)
    #     print(response)
    #     # wiringpi.digitalWrite(ledPin, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
    #     sleep(1)                 # wait half a second  
    #     # wiringpi.digitalWrite(ledPin, 0)         # set GPIO24 to 0/GPIO.LOW/False  
    #     sleep(1)                 # wait half a second
    #print(bin(leds.outputData())) 
    leds.fill(RGBdata(255,0,0,100))     
    buf = bytes(leds.ws2812_Data())
    print(buf)
    spi.xfer2(buf)
    time.sleep(10)

    leds.fill(RGBdata(0,255,0,100))
    buf = bytes(leds.ws2812_Data())
    print(buf)
    spi.xfer2(buf)
    time.sleep(10)

    leds.fill(RGBdata(0,0,255,100))
    buf = bytes(leds.ws2812_Data())
    print(buf)
    spi.xfer2(buf)
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program



