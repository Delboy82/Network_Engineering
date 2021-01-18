import csv
import json



def csvtojson(csv_file,json_file):
	# set x to 0
	x = 0

	#open csv file with Reader and skip first row
	with open(csv_file) as f:
		csv_reader = csv.reader(f)
		next(csv_reader)
	#Create dictonary set index key and create a list
		data = {"name": []}
	#for each row in the csv append to the dictonary
		for rows in csv_reader:
			data["name"].append({"name": rows[0], "description": rows[1], "type": rows[2], "url": rows[3]})

	#Write the date to json file
	with open(json_file, 'w') as jsonf:
		jsonf.write((json.dumps(data["name"], indent=2)))

	jsondata = json.dumps(data["name"], indent=2)
	
	return (jsondata)
