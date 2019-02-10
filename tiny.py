import requests
import os
import sys, re

C = '\033[36m' # cyan

def banner():
	print ("""
╔═╗╦ ╦╔═╗╦═╗╔╦╗╔═╗╔═╗╦╔═ c0d3d by : Zekkel AR
╚═╗╠═╣║ ║╠╦╝ ║ ╔═╝║╣ ╠╩╗
╚═╝╩ ╩╚═╝╩╚═ ╩ ╚═╝╚═╝╩ ╩
Aalex, Faisal, Agung, ramdan19, sulton, nurdin, dani, magisya
""")

class a:
	def __init__(self):
		self.url = input("url => ")
		print ("====== SHORTLINK ======")
	def haha(self):
		apaan = ('https://tinyurl.com/create.php?source=&url=%s&submit=Make+TinyURL!&alias=' % self.url)
		gapapa = requests.get(apaan).text
		yaudah = re.findall(r'<b>(.*?)</b>', gapapa)
		for c in yaudah:
			c = c.strip()
			result = c.split("Enter a long URL to make tiny:")
			print (""+C+"")
			print (result)

if __name__ == "__main__":
	os.system('clear')
	banner()
	zek = a()
	zek.haha()