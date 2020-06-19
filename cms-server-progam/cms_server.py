from flask import Flask, render_template, request
from forms import ConfigForm
from forms import RequestForm
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] ='altintra'


#hardcoding some variables because no front end 
live_devices = ["device_5"]    
device_config_details = {
			"sensor_sensitivity": 7,
			"amount_dispensed": 50
						}

config_result = {}
request_result = {}

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/config", methods=['GET', 'POST'])
def config():
	form = ConfigForm()
	if form.is_submitted():
		config_result = request.form
		
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


