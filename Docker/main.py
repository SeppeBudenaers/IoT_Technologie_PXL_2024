import argparse 
import os
secret = os.environ.get('API_KEY')
print(secret + "OS")

parser = argparse.ArgumentParser(description='IOT program')
parser.add_argument('API_KEY', metavar='API_KEY',type=str, help='enter your API key')
args = parser.parse_args()

API_KEY = args.API_KEY

print(API_KEY + "ARGPARSE")