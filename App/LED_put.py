import requests
import argparse

def GetAPIKEYFile(file_path:str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

parser = argparse.ArgumentParser(description='IOT program')
parser.add_argument('RED', metavar='RED', type=int, help='enter red')
parser.add_argument('GREEN', metavar='GREEN', type=int, help='enter green')
parser.add_argument('BLUE', metavar='BLUE', type=int, help='enter blue')
parser.add_argument('BRIGHTNESS', metavar='BRIGHTNESS', type=int, help='enter Brightness')
args = parser.parse_args()
API_KEY = GetAPIKEYFile("apikey.txt")
url = 'http://iot.pxl.bjth.xyz/api/v1/LED'
headers = {
    'X-Api-Key': str(API_KEY)  # Fix the header format
}



# main loop
data = {
    "R": args.RED,
    "G": args.GREEN,
    "B": args.BLUE,
    "Brightness": args.BRIGHTNESS
}
RGBSend = requests.put(url, json=data, headers=headers)
if RGBSend.status_code != 200:
    print("error : "+ str(RGBSend.status_code))

