import csv
from jinja2 import Template


def SwitchModel():
	menu = {}
	menu['1']="Cisco Catalyst 9200 Series" 
	menu['2']="Cisco Catalyst 2960 Series"
	while True: 
		#options=menu.keys()
		#options.sort()
		for entry in menu: 
			print (entry, menu[entry])
		
		selection=input("Please Select Model:")
		if selection =='1':
			print ("Building Cisco 9200 Series Configs from CSV")
			TemplateFile = "9200_config.j2"
			ConfigGenerator(TemplateFile)
		elif selection == '2':
			print ("Building Cisco 2960 Series Configs from CSV")
			TemplateFile = "2960x_config.j2"
			ConfigGenerator(TemplateFile)
		else:
			print ("Unknown Option Selected!")
		#break 	



def ConfigGenerator(TemplateFile):
	with open("data.csv", "r") as file:
		csvfile = csv.reader(file)
		next(csvfile, None)
		for row in csvfile:
			hostname = row[0]
			location = row[1]
			manip = row[2]
			enablesecret = row[3]
			bvadminsecret = row[4]
			dhcpsnoopingvlans = row[5]
			manvlan = row[6]
			mansubnet = row[7]
			gateway = row[8]
			snmpstring = row[9]
			localsitedc = row[10]
			radkey = row[11]
			vtpdomain = row[12]
			vtppassword = row[13]
			vtpversion = row[14]
			snmpv3 = row[15]
			smarttoken = row[16]

			with open(TemplateFile, 'r') as config_file:
				template_file = config_file.read()

				tm = Template (template_file)

				msg = tm.render(hostname=hostname, location=location, vtpdomain=vtpdomain, vtppassword=vtppassword, vtpversion=vtpversion, manip=manip, enablesecret=enablesecret, bvadminsecret=bvadminsecret, manvlan=manvlan, mansubnet=mansubnet, gateway=gateway, snmpstring=snmpstring, localsitedc=localsitedc, radkey=radkey, snmpv3=snmpv3, smarttoken=smarttoken)

	

				with open(hostname+".txt", 'w') as output:
					output.write(msg)

SwitchModel()
