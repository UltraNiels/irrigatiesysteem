# import RPi.GPIO as GPIO
import config
from time import sleep


def pump():
	c = config.load()

	pin = c['pump_relay_pin']

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)

	GPIO.output(pin, GPIO.HIGH) # turn on pump
	sleep(c['pump_time'] / 1000)
	GPIO.output(pin, GPIO.LOW) # turn off pump

	GPIO.cleanup()

if __name__ == '__main__':
	pump()