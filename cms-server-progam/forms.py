from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField



class ConfigForm(FlaskForm):
	device_name = StringField('device name')
	sensor_sensitivity = StringField('sensor sensitivity')
	liquid_dispensed = StringField('liquid dispensed')
	submit = SubmitField('submit')

class RequestForm(FlaskForm):
	device_name = StringField('device name')
	submit = SubmitField('submit')