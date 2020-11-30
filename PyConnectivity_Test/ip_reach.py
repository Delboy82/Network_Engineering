import subprocess
import sys
import time
from prettytable import PrettyTable

def ip_reach(ip_list):
	t = PrettyTable()
	timestr = time.strftime("%d%m%Y-%H%M%S")
	datestr = time.strftime("%d%m%Y")
	for ip in ip_list:
		t.field_names = ["Endpoint", "Status Up/Down"]
		ip = ip.rstrip("\n")
		command_line = ['ping', '-c1', ip]
		ping_reply = subprocess.Popen(command_line, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
		ping_reply.wait()
		if ping_reply.poll() == 0:
			t.add_row([ip, "Up"])
			#print ("\n* {} is Alive\n".format(ip))
			result = 'logs/'+timestr+'_sucess_file.txt'
			file = open(result, 'a')
			file.write("* {} is Alive\n".format(ip))
			file.close
		else:
			t.add_row([ip, "Down"])
			#print("\n* {} is Dead\n".format(ip))
			result = 'logs/'+timestr+'_failure_file.txt'
			file = open(result, 'a')
			file.write("* {} is Dead\n".format(ip))
			file.close
	print(t)
	sys.exit()
