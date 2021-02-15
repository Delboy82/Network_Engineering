### written using python3.6

import requests
import json
import banner
from prettytable import PrettyTable
from getpass import getpass 
import CsvToJson
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

banner.main_banner()

ipaddr = input("Enter FMC IP address: ")
username = input("Enter FMC Username: ")
password = getpass()
filecsv = input("Enter CSV file name example: data/HostObjects.csv:  ")
filejson = input("Enter Ouput name for  JSON file example data/json/RB251110.json: ")

server = "https://"+ipaddr

headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path

r = requests.post(auth_url, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)

domainuuid = r.headers["DOMAIN_UUID"]

apiurl = "/api/fmc_config/v1/domain/" + domainuuid + "/object/hosts?bulk=true" 
url = server + apiurl
headers =   {"Content-Type": "application/json", "X-auth-access-token":  r.headers["X-auth-access-token"]}

json_payload = CsvToJson.csvtojson(filecsv, filejson)

x = requests.post(url, headers=headers, data = json_payload, verify=False)

if x.status_code == 201 or x.status_code == 202:
	print ("Objects Successfully Created")
else:
	print ("Object Creation Failed Status Code: %s" % (x.status_code))
