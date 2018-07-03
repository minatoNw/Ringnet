import socket
import threading
import console
import recv
import conn


host_ip = socket.gethostbyname(socket.gethostname())
port = 1890

print("host:{}:{}".format(host_ip, port))

console.console()
