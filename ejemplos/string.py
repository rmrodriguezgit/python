#/usr/bin/env python
#_*_ coding: utf8 _*_

saludo = "Hola Usuario"

print(type(saludo))

entero = 10

print(type(entero))

flotantes = 3.1416

print(type(flotantes))


if entero < 0:
    print ("Negativo")
elif entero > 0:
    print ("Positivo")
else:
    print ("Cero")

num = 11
var = "par" if (num % 2 == 0) else "impar"

print (var)


l = [22, True, "una lista", [1, 2]]
print (l)
print (l[0])

fav="hola.net"

if fav == "mundogeek.net":
 print ("Tienes buen gusto!")
 print ("Gracias")
if fav != "mundogeek.net":
 print ("Vaya, que lástima")
