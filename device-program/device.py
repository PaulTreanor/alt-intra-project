import socket
from flask import Flask
import time
from threading import Thread
import urllib
cms_ip =""
file = ""
id_no = ""

#device finding its own ip
def find(hostname, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.25)
	conn = s.connect_ex((hostname, port))
	s.close()
	return conn == 0


#device searching for the cms
def search():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	device_ip = s.getsockname()[0]
	ip = device_ip[0:10]
	s.close()
	for i in range(0,255):
		print(ip+str(i))
		res = find(ip+str(i), 5770)
		if res:
			print("Device found at: ", ip+str(i) + ":"+str(5770))
			global cms_ip
			cms_ip = ip+str(i)
			return 1
	else:
		return 0

def runserver():
	app.run(host= '0.0.0.0')

#updating the stats webpage based on the stats file
def stat_updater():
	while True:
		print("Updating device data")
		f = open("stats.txt", "r")
		global file
		file = f.read()
		time.sleep(10)

#updating the config file based on the cms webpage
def config_updater():
	while True:
		print("Updating Configuration File")
		link =  "http://" + cms_ip + ":5000" + "/cms/device_config/" +"device"+id_no
		l = urllib.request.urlopen(link)           
		condata = l.read().decode()  
		f = open("config.txt", "w")
		f.write(condata)
		f.close()
		time.sleep(30)


app = Flask(__name__)
@app.route('/device/device_data')
def index():
	return file

#device running reading the stats file and starting the app, stat and config threads
f = open("stats.txt", "r")
file = f.read()
k = file.split(",")[0]
id_no = k.split(":")[1].strip(" ")
f.close()
Thread(target=runserver).start()
ser = 0
while not ser:
	ser = search()
Thread(target=stat_updater).start()
Thread(target=config_updater).start()











