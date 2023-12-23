import argparse 
import requests
import time
import os
API = os.environ.get('API_KEY')
print(API + " OS")

url = 'http://iot.pxl.bjth.xyz/api/v1/temperature' 
data = {

 "id": time.time(),

 "value": 25.5,

 "scale": "F"

}
headers = {
    'X-Api-Key': API,
    'Content-Type': 'application/json'
}

response = requests.put(url, headers=headers, json=data)

print(response)

parser = argparse.ArgumentParser(description='IOT program')
parser.add_argument('API_KEY', metavar='API_KEY',type=str, help='enter your API key')
args = parser.parse_args()

API_KEY = args.API_KEY

print(API_KEY + " ARGPARSE")