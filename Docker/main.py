from led import RGBdata, Neopixel
import spidev
import argparse
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
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
API_KEY = GetAPIKEYFile("secretfile.txt") # Getting the apikey from docker secrets
url = 'http://iot.pxl.bjth.xyz/api/v1/LED'# the api url
headers = {'X-Api-Key': str(API_KEY)}

# Session with retry logic
session = requests.Session()
retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

#SPI
spi = spidev.SpiDev()
spi.open(0,0) # open /dev/spidev0.0
spi.mode = 0b00
spi.max_speed_hz = 6000000*2

#NeoPixel
leds = Neopixel(1)
leds.fill(RGBdata(255, 200, 0, 100))
print(leds.colors())
oldData = RGBdata(0,0,0,0)
newData = RGBdata(0,0,0,0)

# main loop
try:
    while(1):
        time.sleep(0.5) # A delay for not ddos'ing bryan's server
        
        RGBRecieve = session.get(url, headers=headers, timeout=2) # sending GET request to API
        if RGBRecieve.status_code != 408: # timeout response
            RGBRecieve.raise_for_status()  # This will raise an HTTPError for bad responses (status codes 4xx and 5xx)
            
        LED = json.loads(RGBRecieve.json()) # converting json to struct
        
        newData = RGBdata(LED['R'], LED['G'], LED['B'], LED['Brightness']) # converting struct to RGBdata dataclass
        
        if newData != oldData: #ignoring same data
            
            leds.fill(newData) # changing color
            spi.writebytes2(leds.ws2812_Data())            
            oldData = newData 
            
# error handling
except requests.exceptions.RequestException as e:
    print("Request failed:", str(e))
except json.JSONDecodeError as e:
    print("JSON decoding failed:", str(e))
except requests.exceptions.HTTPError as e:
    print("HTTP error:", str(e))
except Exception as e:
    print("An unexpected error occurred:", str(e))
    
leds.fill(RGBdata(0,0,0,0))
spi.writebytes2(leds.ws2812_Data())