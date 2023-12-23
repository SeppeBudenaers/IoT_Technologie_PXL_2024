import argparse
import requests
import time
import httplib
# import os

# def GetAPIKEYOS():
#     try:
#         # API_KEY = os.environ.get('API_KEY')
#         return API_KEY
#     except KeyError:
#         print("Environmental Key Does not exist")

def GetAPIKEYARG():
    parser = argparse.ArgumentParser(description='IOT program')
    parser.add_argument('API_KEY', metavar='API_KEY', type=str, help='enter your API key')
    args = parser.parse_args()
    return args.API_KEY

def GetAPIKEYFile(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(str(content) + "content")
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Choose one of the methods to get API_KEY
# API_KEY = GetAPIKEYOS()
# API_KEY = GetAPIKEYARG()
API_KEY = GetAPIKEYFile("secretfile.txt")
print(str(API_KEY) + " APIKEY")

url = 'http://iot.pxl.bjth.xyz'
data = {
    "id": time.time(),
    "value": 25.5,
    "scale": "F"
}
connection =  httplib.HTTPConnection('1.2.3.4:1234')
connection.request('PUT','-H X-Api-Key: '+str(API_KEY),'/api/v1/temperature', data)
result = connection.getresponse()
print(result)

data.id +1
headers = {
    '-h':"X-Api-Key: "+str(API_KEY)  # Fix the key here
}

response = requests.put(url, json=data, headers=headers)

print(response)