from flask import Flask, render_template, request
from forms import ConfigForm
from forms import RequestForm
from threading import Thread
import pickle
import socket


app = Flask(__name__)
app.config['SECRET_KEY'] ='altintra'

#default configuration for devices [solution dispensed, sensor sensitivity]
global config_result
config_result = {
	"device1" : [50, 75],
	"device2" : [50, 75],
	"device3" : [50, 75],
	"device4" : [50, 75],
	"device5" : [50, 75]
}

@app.route("/")
def home():
	return render_template('index.html')

#device configuration form
@app.route("/config", methods=['GET', 'POST'])
def config():
	form = ConfigForm()
	if form.is_submitted():
		#submitted data 
		form_results = request.form
		device_name = form_results["device_name"]
		solution_dispensed = form_results["liquid_dispensed"]
		sensor_sensitivity = form_results["sensor_sensitivity"]

		#search for device name in global config results 
		global config_result 
		if device_name in config_result:
			config_result[device_name] = [solution_dispensed, sensor_sensitivity]
	return render_template('config.html', form=form)

#request device data
@app.route("/request", methods=['GET', 'POST'])
def request_data():
	form = RequestForm()
	if form.is_submitted():
		request_result = request.form
		return render_template("urlsuppliedbynevan/<request_result>")
	return render_template('request.html', form=form)


#put new config to a api url 
@app.route('/device_config/<device_id>')
def update_device_config(device_id):
	device_id = device_id.replace("_", " ")
	return "".join(str(config_result[device_id]))
    
    
#Added to connect device and cms    
def run_server():
    app.run(host = '0.0.0.0')
    
def listen_device():
    HOST = ''
    PORT = 5770

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((HOST,PORT))
        
    except socket.error as msg:
        print('Bind Failed. Error Code : ' + str(msg[0]) + 'Message' + msg[1])
        sys.exit()

    print('Socket bind complete')

    while True:
        s.listen()
        conn,addr = s.accept()
        print( 'Connected with ' + addr[0] + ':' + str(addr[1]))
        #addr0 is the ip
		data = conn.recv(1024).decode()
    
if __name__ == '__main__':
    Thread(target=run_server).start()
    Thread(target=listen_device).start()
    



