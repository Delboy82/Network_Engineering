import requests
import json
import os


def Auth():
   #Authenticate API access and receive access Token

   user = os.getenv("IQ_USERNAME")
   passwd = os.getenv("IQ_PASSWORD")

   url = "https://api.extremecloudiq.com/login"

   payload = json.dumps({
      "username": user,
      "password": passwd
   })

   headers = {
        'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)
   data = response.json()
   data = data["access_token"]
   
   return (data)
