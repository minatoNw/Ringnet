import socket

def recv():
	host = socket.gethostbyname(socket.gethostname())
	port = 1890

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('', port))
	sock.listen(2)

	print("waiting connection")
	conn, addr = sock.accept()
	print("[conn] {}:{}".format(addr[0], addr[1]))
	while True:
		data = conn.recv(4096)
		print("[recv] {}".format(data.decode()))
	sock.shutdown(1)
	sock.close()
