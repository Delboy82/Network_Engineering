from  ExtremeIQAuth import Auth
import requests
import json



'''This script pulls a list of offline devices and prints the output to the screen.'''


token = Auth()

def getdevice(token):
   token = token

   url = "https://api.extremecloudiq.com/devices?page1&limit=100&connected=false"
   
   headers = {
      "Authorization": "Bearer "+token,
      "Content-Type": "application/json"
   }

   response = requests.request("GET", url, headers=headers)

   payload = json.loads(response.text)

   for i in range (len(payload["data"])):
      print ("Hostname: "+payload["data"][i]["hostname"])
      print ("Serial Number: "+payload["data"][i]["serial_number"])
      print ("Mac Address: "+payload["data"][i]["mac_address"])
      print ("Model: "+payload["data"][i]["product_type"])
      print ("Last Seen: "+payload["data"][i]["last_connect_time"]+"\n")
      

getdevice(token)
