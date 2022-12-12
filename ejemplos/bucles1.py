#/usr/bin/env python
#_*_ coding: utf8 _*_

import io

edad = 0
while edad < 24: 
	edad = edad + 1

print ( 'Felicidades, tienes ' + str(edad) )

n = 0
while n < 10:
	n = n + 1

print (n)

#serie del 5, 5 10 15 20 25 30 35 40 45 ... 100

s = 0
while s < 100:
	s = s + 5 
	print (s)

# Ciclo infinito... bueno casi
while True:
	entrada = input(">>> ")
	if entrada == 'quit()':
		break
	else:
		print( entrada )


