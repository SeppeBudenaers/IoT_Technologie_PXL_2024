from led import RGBdata, Neopixel
import argparse
import requests
import json
import time
from time import sleep
import os

API_KEY = #your api key
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
