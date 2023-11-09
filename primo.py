n=int(input('Ingrese el numero entero: '))
cont=0
for i in range(1,n+1):
	if n%i==0:
		cont+=1

if cont==2:
	print('El numero SI es primo')
else:
	print('El numero NO es primo')
