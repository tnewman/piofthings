from piot.sensor.baseanalogsensor import BaseAnalogSensor
from piot.sensor.basedigitalsensor import BaseDigitalSensor
import importlib
import pkgutil
import os

plugin_directory=os.path.dirname(__file__)

#Load all of the modules in this package
for module in pkgutil.iter_modules([plugin_directory]):
	name_index=1
	importlib.import_module('.' + module[name_index], __package__)

def get_analog_sensor_classes():
	return BaseAnalogSensor.__subclasses__()

def get_digital_sensor_classes():
	return BaseDigitalSensor.__subclasses__()