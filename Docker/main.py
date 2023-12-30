from led import RGBdata, Neopixel
import spidev
import argparse
import requests
import json
import time
from time import sleep
import os

def GetAPIKEYFile(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()  # Remove leading/trailing whitespaces
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

#api 
API_KEY = GetAPIKEYFile("secretfile.txt")
print(API_KEY)
url = 'http://iot.pxl.bjth.xyz/api/v1/LED'
headers = {
    'X-Api-Key': str(API_KEY)  # Fix the header format
}

#SPI
spi = spidev.SpiDev()
spi.open(0,0) # open /dev/spidev0.0
spi.mode = 0b00
spi.max_speed_hz = 6000000*2

#NeoPixel
leds = Neopixel(1)
leds.fill(RGBdata(300, 200, 0, 100))
print(leds.colors())

# main loop
data = {
    "R": 255,
    "G": 50,
    "B": 0,
    "Brightness": 255
}
RGBSend = requests.put(url, json=data, headers=headers)
if RGBSend.status_code != 200:
    print("error : " + str(RGBSend.status_code))

RGBRecieve = requests.get(url, headers=headers)
if RGBRecieve.status_code != 200:
    print("error : " + str(RGBRecieve.status_code))

LED = json.loads(RGBRecieve.json())
leds.fill(RGBdata(LED['R'], LED['G'], LED['B'], LED['Brightness']))
print(leds.colors())
buf = bytes(leds.ws2812_Data())
print(buf)
spi.writebytes2(buf)
