import numpy

if __name__ == '__main__':
	numbuscar = int()
	n = int()
	nencontrado = bool()
	nencontrado = False
	n = 0
	print("Ingrese el tamaño del vector")
	n = int(input())
	vector = numpy.zeros([n],dtype=int)
	print("Ingrese los valores del vector")
	for i in range(n):
		print("Ingrese el elemento A [",i,"] ")
		vector[i] = input()
	print("Ingresar el numero que desea verificar si se encuentra en el vector ingresado anteriormente")
	numbuscar = int(input())
	if (n>=10):
		for i in range(0,10,1):
			if vector[i]==numbuscar:
				nencontrado = True
				if nencontrado==True:
					print("El numero ",numbuscar," si se encuentra en el vector, en la posicion ",i)
				else:
					print("El numero ",numbuscar," no se encuentra en el vector")
	if (n<10):
		for i in range(n):
			if vector[i]==numbuscar:
				nencontrado = True
				if nencontrado==True:
					print("El numero ",numbuscar," si se encuentra en el vector, en la posicion ",i)
				else:
					print("El numero ",numbuscar," no se encuentra en el vector")

