#/usr/bin/env python
#_*_ coding: utf8 _*_

#Funciones

def mi_funcion(param1, param2):
    print(param1)
    print(param2)


mi_funcion('Hola','Mundo')

#Envia 2 variables y súmalas

def sumar(n1, n2):
    print(n1+n2)


sumar(10,20)


#funcion que me regresa el IVA de un producto
def regresaImpuesto(precio):
	print( "El IVA es:", precio*0.16 )

regresaImpuesto(10000)


#realizar una funcion que pida + - * / y dos números
def operadores(op,n1,n2):
    if   op=='+':
    	print ('El resultado es = ',n1+n2)
    elif op == '-':
    	print ('La resta es =', n2-n1)
    elif op == '*':
    	print ('la multiplicación es =',n1*n2)
    elif op == '/':
        print ('La división es =',n2/n1)
    elif op == '%':
        print ('El modulo de la div es =',n2%n1)
    elif op == '//':
    	print ('La división entera es =',n1//n2)
    elif op == '--':
    	print('La * -1 es = ', -n1,-n2)
    else:
    	print('El operador', op, 'no es válido')

operadores('+',20,5)
operadores('-',20,5)
operadores('*',20,5)
operadores('/',20,5)
operadores('%',20,5)
operadores('//',20,5)
operadores('--',20,5)
operadores('&&',20,5)


# = 0.5


