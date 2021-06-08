const socket = io();

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
	console.log(data);
	for (let d in data) {
		try{
		document.getElementById(d).innerHTML = data[d]
		}
		catch{}
	}
})