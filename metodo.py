#Es un ejemplo de como se ejecuta una función

def suma(x,y):
	return x+y 

def facto(n):
	if n<0:
		return('ERROR')

	if n==0 or  n==1:
		return 1
	else:
		return n*facto(n-1)


def factoi(n):
	if n<0:
		return ('ERROR')
	else:
		var=1
		for i in range(1, n+1):
			var*=i
		return var



n=int(input('Ingrese el numero entero: '))
print('El factorial de: ', n, 'es: ', facto(n))
print('-----------------------------')
print('El factorial iterativo de: ', n , 'es: ', factoi(n))

