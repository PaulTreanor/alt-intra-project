from flask import Flask, render_template, request
from forms import ConfigForm
from forms import RequestForm
app = Flask(__name__)
app.config['SECRET_KEY'] ='altintra'

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

if __name__ == '__main__':
    app.run(debug=True)


