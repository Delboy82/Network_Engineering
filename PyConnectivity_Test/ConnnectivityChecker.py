import ip_reach as p


def openfile():
	host_file = input ("Enter the name of the ip address file example ip_file.txt: ")
	file = open(host_file, 'r')
	file.seek(0)
	ip_list = file.readlines()
	file.close
	return ip_list

iplist = openfile()
p.ip_reach(iplist)



