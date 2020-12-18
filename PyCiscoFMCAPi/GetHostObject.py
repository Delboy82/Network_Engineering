### written using python3.6

import requests
import json
from prettytable import PrettyTable
from getpass import getpass 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


ipaddr = input("Enter FMC IP address: ")
username = input("Enter FMC Username: ")
password = getpass()

server = "https://"+ipaddr

headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path

#r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)

r = requests.post(auth_url, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)

#print ("***** Printing Header Information ****")
#print ("X-auth-access-token: "+r.headers["X-auth-access-token"])
#print ("DOMAIN_UUIS: "+r.headers["DOMAIN_UUID"])
#print ("X-auth-refresh-token: "+r.headers["X-auth-refresh-token"])

domainuuid = r.headers["DOMAIN_UUID"]
#apiurl = "/api/fmc_config/v1/domain/"+domainuuid+"/object/fqdns" 
#apiurl = "/api/fmc_config/v1/domain/"+domainuuid+"/object/networks"
apiurl = "/api/fmc_config/v1/domain/"+domainuuid+"/object/hosts?expanded=true" 
url = server + apiurl
headers =   {"Content-Type": "application/json",
             "X-auth-access-token":  r.headers["X-auth-access-token"]
             }

x = requests.get(url, headers=headers, auth=requests.auth.HTTPBasicAuth(username,password), verify=False)

json_data = json.loads(x.text)

t = PrettyTable()

t.field_names = ["Name", "Type", "Value", "Description"]


for i in range(len(json_data["items"])):
	t.add_row([json_data["items"][i]["name"], 
	json_data["items"][i]["type"], 
	json_data["items"][i]["value"], 
	json_data["items"][i]["description"]])          
            # print (json_data["items"][i]["name"])
            # print (json_data["items"][i]["type"])

print (t)
