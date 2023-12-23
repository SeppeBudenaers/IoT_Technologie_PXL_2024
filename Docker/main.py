import argparse 
import requests
import time
import os
def GetAPIKEYOS():
    try:
        API_KEY = os.environ.get('API_KEY')
        return API_KEY  
    except KeyError:
        print(f"Enviormental Key Does not exist")

def GetAPIKEYARG():
    parser = argparse.ArgumentParser(description='IOT program')
    parser.add_argument('API_KEY', metavar='API_KEY',type=str, help='enter your API key')
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

API_key = GetAPIKEYFile("./secretfile.txt")
print(API_KEY)

url = 'http://iot.pxl.bjth.xyz/api/v1/temperature' 
data = {

 "id": time.time(),

 "value": 25.5,

 "scale": "F"

}
headers = {
    '-h X-Api-Key': API_KEY
}

response = requests.put(url, json=data, headers=headers)

print(response)
