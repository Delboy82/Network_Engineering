from prettytable import PrettyTable
import requests
import json
import ipaddress

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"


response = requests.get(url, verify=False)


json_data = json.loads(response.text)


def ListAWSServices():
	##List Services
	t = PrettyTable()
	t.field_names = ["Service"]
	mylist = []
	for item in json_data["prefixes"]:
		mylist.append(item["service"])

	
	newlist = list(set(mylist))
	
	newlist.sort()
	for item in newlist:
		print (item)

def ListAWSRegions():
	t = PrettyTable()
	t.field_names = ["Regions"]
	regionlist = []
	for item in json_data["prefixes"]:
		regionlist.append(item["region"])

	regionlist = list(set(regionlist))

	regionlist.sort()
	for item in regionlist:
		print (item)

def ListAWSIPranges():
	IPrange = []
	t = PrettyTable()
	t.field_names = ["IP Prefix", "Region", "Service", "Network Border Group"]
	
	serv = input("\n\nEnter Service name: ")
	regi = input ("Enter Region: ")	

	for item in json_data["prefixes"]:
		if item["service"] == serv and item["region"] == regi:
			t.add_row([item["ip_prefix"], item["region"], item["service"], item["network_border_group"]])
	print (t)
	return (json_data, serv, regi)

def ASA_Config_Generator(ipprefix):
	
	with open("ASA_CONFIG.txt", 'a') as outputfile:
		for item in ipprefix[0]["prefixes"]:
			if item["service"] == ipprefix[1] and item["region"] == ipprefix[2]:
				addr = ipaddress.ip_network(item["ip_prefix"])
				outputfile.write ("Object network "+ipprefix[1]+"_"+str(addr.network_address))
				outputfile.write ("\n\tsubnet "+str(addr.network_address)+" "+str(addr.netmask))
				outputfile.write ("\n\tdescription "+ipprefix[1]+" "+ipprefix[2])
				outputfile.write ("\n\n")

ListAWSServices()
ListAWSRegions() 
ipprefix = ListAWSIPranges()
ASA_Config_Generator(ipprefix)


