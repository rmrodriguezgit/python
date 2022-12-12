
# En esta parte de solicita la entrada de las
# variables por medio del teclado
# y se almacenan en la variable
producto = input('Introduce el producto:')
precio = int (input('$:'))
desc = int (input('Desc %:'))

#Aquí se define la función a realizar
def imprimeDescuento( precio, desc) :
	print (precio*(1-(desc/100)))

#Se ejecuta la función
print ('El producto', producto, 
	   'con valor de $:', precio)
print ('Descuento de $')
imprimeDescuento( precio, desc)