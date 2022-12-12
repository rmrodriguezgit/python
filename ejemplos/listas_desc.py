#https://medium.com/@hgodinez89/operaciones-sobre-listas-en-python-c19853a9d07b

x = ['123456',100,0.02,'345678',90,0.05,
     '987654',75,0.03,'91119',120,0.25,
     '82228',93,0.03,'71117',7,0]

suma = 0

def calculaDescuento(p, d):
	return p*(1-d)

while True:
	codigo = input(">>")
	if codigo == '0':
	   break
	if codigo in x:
		suma = suma + calculaDescuento(x[x.index(codigo)+1],x[x.index(codigo)+2])
	else:
		print('Llamar al supervisor código inexistente', codigo)
	


print ('El total con desc es:',suma)

