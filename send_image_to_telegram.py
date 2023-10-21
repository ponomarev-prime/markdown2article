import requests
import os
import json
import sys
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
chat_id = os.getenv('ID')

args = sys.argv[1:]
message = args[0]

img_path='image.png'
image_caption=message

url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

data = {"chat_id": chat_id, "caption": image_caption} #  "message_thread_id": 4 for super

with open(img_path, "rb") as image_file:
    responseData = requests.post(url, data=data, files={"photo": image_file}).json()

json_string = json.dumps(responseData)
print(json_string)