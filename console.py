import socket
import threading
import conn
import recv

name = "ringnet"
prompts = ['>', '#', '(config)#', '(config-sock-recv)#', '(config-sock-send)#']
mode = 0

recv_port = 1890

def console():
	while True:
		prompt = prompts[mode]
		line = input(name + prompt)
		if not shellrun(line):
			break

def shellrun(line):
	global prompts
	global mode
	global name
	cmd = line.split()
	print(cmd)
	if len(cmd) == 0:
		return True
	if mode == 0:
		if cmd[0] == 'enable':
			mode += 1
		if cmd[0] == 'send':
			if len(cmd) != 2:
				print("[E] Invalid Argument")
			else:
				conn.send(cmd[1])
		elif cmd[0] == 'exit':
			return False
	elif mode == 1:
		if cmd[0] == 'config':
			mode += 1
		elif cmd[0] == 'exit':
			mode -= 1
	elif mode == 2:
		if cmd[0] == 'sock':
			if cmd[1] == 'recv':
				mode += 1
			elif cmd[1] == 'send':
				mode += 2
		elif cmd[0] == 'hostname':
			if len(cmd) == 2:
				name = cmd[1]
			else:
				print("[E] Invalid Argument"
		elif cmd[0] == 'exit':
			mode -= 1
	elif mode == 3:
		# configure recv socket
		if cmd[0] == 'exit':
			mode = 2
		elif cmd[0] == "conn":
			if len(cmd) != 3:
				print("[E] Invalid Argument")
		elif cmd[0] == 'acpt':
			if len(cmd) == 2:	# ポート指定
				port = int(cmd[1])
			th_recv = threading.Thread(target=recv.recv, args=(port))
			th_recv.setDaemon(True)
			th_recv.start()
	elif mode == 4:
		# configure send socket
		if cmd[0] == 'exit':
			mode = 2
		elif cmd[0] == 'conn':
			if len(cmd) != 3:
				print("[E] Invalid Argument")
			else:
				conn.conn(cmd[1], int(cmd[2]))
	return True
	"""
	if cmd[0] == 'send':
		conn.send(cmd[1])
	elif cmd[0] == 'conn':
		print(cmd)
		print("connecting... {}:{}".format(cmd[1], cmd[2]))
		try:
			conn.conn(cmd[1], int(cmd[2]))
		except:
			print("error")
	elif cmd[0] == 'exit':
		return False
	"""
