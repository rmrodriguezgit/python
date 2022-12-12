#/usr/bin/env python
#_*_ coding: utf8 _*_

super = []
lista= 'Lista de Compras'

while True:
	lista = input(">>")
	super.append(lista)
	if lista == "s":
		break
super.remove('s')
print (super)

