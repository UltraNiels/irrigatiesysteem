import eventlet
import socketio
import config
import threading
import time
import pump

active_clients = 0

c = config.load()
d = config.loaddata()

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
   	sio.emit('Data!', dict(c, **d), room=sid)
   	print('datataa')

@sio.on('pump_now')
def pump_now(sid):
	pump.pump()
	d['times_pumped'] += 1
	config.writedata()

@sio.event
def poweroff(sid):
	subprocess.run(["shutdown", "now"])

@sio.event
def reboot(sid):
	subprocess.run(["reboot"])

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

def run():
	eventlet.wsgi.server(eventlet.listen(('', 80)), app)

run()

thr = threading.Thread(target=run, args=(), kwargs={})