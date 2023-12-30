from led import RGBdata, Neopixel
import argparse
import requests
import json
import time
from time import sleep
import os

def GetAPIKEYFile(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

leds = Neopixel(1)
leds.fill(RGBdata(300,200,0,100))
print(leds.colors()) 

API_KEY = GetAPIKEYFile("secretfile.txt")
print(API_KEY)
url = 'http://iot.pxl.bjth.xyz/api/v1/LED'
headers = {
    'X-Api-Key': str(API_KEY)  # Fix the header format
}

# main loop
data = {
    "R": 255,
    "G": 0,
    "B": 255,
    "Brightness": 0
}
RGBSend = requests.put(url, json=data, headers=headers)
if RGBSend.status_code != 200:
    print("error : "+ str(RGBSend.status_code))

RGBRecieve = requests.get(url, headers=headers)
if RGBRecieve.status_code != 200:
    print("error : "+ str(RGBRecieve.status_code))

LED = json.loads(RGBRecieve.json())
leds.fill(RGBdata(LED['R'],LED['G'],LED['B'],LED['Brightness']))
print(leds.colors()) 
