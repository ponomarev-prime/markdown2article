
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

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
responseData = requests.get(url).json()

json_string = json.dumps(responseData)
print(json_string)