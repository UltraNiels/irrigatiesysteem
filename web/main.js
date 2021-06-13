const socket = io();
let data = {};

socket.emit('Hello?')

const ask = () => {
	socket.emit('Data?');
	console.log('ask')
}

socket.on('Hello!', () => {
	console.log('helo');
	setInterval(ask, 1000)
})

socket.on('Data!', data => {
	d = data;
	for (let d in data) {
		try{
		document.getElementById(d).innerHTML = data[d]
		}
		catch{}
	}
})

function edit()	{
	
}

document.getElementById('edit').addEventListener('click', edit)
document.getElementById('poweroff').addEventListener('click', ()=>socket.emit('poweroff'))
document.getElementById('reboot').addEventListener('click', ()=>socket.emit('reboot'))
