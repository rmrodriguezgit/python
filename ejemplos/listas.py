#https://medium.com/@hgodinez89/operaciones-sobre-listas-en-python-c19853a9d07b

x = ['123456',100,'345678',90,'987654',75,'91119',120,'82228',93,'71117',7]

suma = 0

while True:
	codigo = input(">>")
	if codigo in x:
		suma = suma + x[x.index(codigo)+1]
	if codigo == '0':
	   break


print ('El total de los productos es:',suma)

