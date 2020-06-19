from flask import Flask, render_template, request
from forms import ConfigForm
from forms import RequestForm
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] ='altintra'

#default configuration for devices [solution dispensed, sensor sensitivity]
global config_result
config_result = {
	"device 1" : [50, 75],
	"device 2" : [50, 75],
	"device 3" : [50, 75],
	"device 4" : [50, 75],
	"device 5" : [50, 75]
}

request_result = {}

@app.route("/")
def home():
	return render_template('index.html')

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

@app.route("/request", methods=['GET', 'POST'])
def request_data():
	form = RequestForm()
	if form.is_submitted():
		request_result = request.form
	return render_template('request.html', form=form)


#put new config into into a domain . 
@app.route('/cms/device_config/<device_id>')
def update_device_config(device_id):
	return config_result



if __name__ == '__main__':
    app.run(debug=True)


