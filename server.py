import eventlet
import socketio
import config
import threading
import time
import pump
import subprocess
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

c = config.load()
d = config.loaddata()

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
sensor = AnalogIn(ads, ADS.P0)

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './web/index.html',
    '/static': './web'	
})

@sio.event
def connect(sid, environ):
    print('Connection from', sid)

@sio.on('Hello?')
def hello(sid):
   	sio.emit('Hello!', room=sid)
   	print("Hello, ", sid)
   	sio.emit('update', c)

@sio.on('Data?')
def hello(sid):
   	sio.emit('Data!', dict(c, **d, moisture=sensor.value), room=sid)
   	print('datataa')

@sio.on('pump_now')
def pump_now(sid):
	pump.pump()
	d['times_pumped'] += 1
	config.writedata(d)

@sio.event
def poweroff(sid):
	subprocess.run(["shutdown", "now"])

@sio.event
def reboot(sid):
	subprocess.run(["reboot"])

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

def autopump():
	while True:
		if  (time.time() > d["last_time_pumped"] + c["min_interval"]) and (sensor.value > c["threshold"]):
			pump_now()
			d["last_time_pumped"] = time.time()
			config.writedata(d)
		time.sleep(1)

autopump_thr = threading.Thread(target=automump, args=(), kwargs={})

if c["automatic_pumping"]:
	autopump_thr.run()

eventlet.wsgi.server(eventlet.listen(('', 80)), app)
