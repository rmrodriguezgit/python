

# inicializar la variable sumatoria
suma = 0

# Hacer ciclo infinito, hasta que ingrese 0

while True:
	pro = int(input("$:"))
	suma = suma + pro
	if pro == 0:
	   break

def aplicaDescuento(s):
	if s >= 1000:
		return (s*0.10)
	else :
		return 0

importe = suma / 1.16
iva = importe * 0.16

print ('El importe es: $', importe)
print ('El iva es: $', iva )
print ('El total es: $',importe+iva)
print ('tu descuento es: $', 
	    aplicaDescuento(suma) )
