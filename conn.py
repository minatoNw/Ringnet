import socket

conn_sock = None

def conn(ip, port):
    global conn_sock
    conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn_sock.connect((ip, port))
    print("[conn] {}:{}".format(ip, port))

def send(msg):
    if conn_sock != None:
        conn_sock.sendall(msg.encode())
