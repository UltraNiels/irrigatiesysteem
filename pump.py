import RPi.GPIO as GPIO
import yaml
from time import sleep

with open('config.yaml', r) as cf:
	c = yaml.load(cf, Loader=yaml.FullLoader)

pin = c['config']['pump_relay_pin']

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(18, GPIO.HIGH) # turn on pump
sleep(c['config']['pump_time'] / 100)
GPIO.output(18, GPIO.LOW) # turn off pump

