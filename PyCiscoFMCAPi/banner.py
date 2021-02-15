import pyfiglet

def main_banner():
	with open("banner.txt", "r") as file:
		banner_txt = file.read()

	ascii_banner = pyfiglet.figlet_format(banner_txt)
	print (ascii_banner)
