class Producto():
	def __init__(self, producto, precio, descuento):
		self.producto = producto
		self.precio = int(precio)
		self.descuento = float(descuento) 

	def presentaProducto(self):
		print (self.precio)
		print (self.descuento)
		return  self.precio * (1 - self.descuento)


productos = [Producto]

print(type(productos))

productos = [Producto("1234",12,0.02),Producto("1235",13,0.02)]

producto = Producto("1234",12,0.02)

print (productos[1].presentaProducto())

print (productos[0].producto)

suma = 0
while True:
	codigo = input('>>')
	if codigo == '0':
		break
	if codigo in productos:
		suma = suma + productos[productos.index(codigo)].presentaProducto()
	

print (suma)






