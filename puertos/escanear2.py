import socket

for port in range(80,90):
	 s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 result=s.connect_ex(("go.neotic.mx",port))
	 if result == 0:
	 	print(port, "Puerto abierto")
	 else:
	 	print(port, "Puerto no abierto")
	 s.close()
