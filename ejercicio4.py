def encontrarpuntosilla(matriz, tamanio):
	numsillas = int()
	numsillas = 0
	may = [str() for ind0 in range(tamanio)]
	men = [str() for ind0 in range(tamanio)]
	for i in range(tamanio):
		men[i] = matriz[i][0]
		for j in range(tamanio):
			if (i==0):
				may[j] = matriz[i][j]
			else:
				if may[j]<matriz[i][j]:
					may[j] = matriz[i][j]
					if men[i]>matriz[i][j]:
						men[i] = matriz[i][j]
					if may[i]==men[j]:
						numsillas = numsillas+1
						print("Se encontro en la posicion: (",(i+1),",",(j+1),")")
	return numsillas
	
if __name__ == '__main__':
	tamanio = int()
	print("Ingresar el tamaño de la matriz: ")
	tamanio = int(input())
	matriz = [[str() for ind0 in range(tamanio)] for ind1 in range(tamanio)]
	for i in range(tamanio):
		for j in range(tamanio):
			print("Ingresar el elemento de la posicion [",i,"][",j,"]: ")
			matriz[i][j] = input()
	print ("")
	print("MATRIZ INGRESADA")
	for i in range(tamanio):
		for j in range(tamanio):
			print(matriz[i][j]+" ", end="")
		print("")
	psilla = int()
	print ("")
	psilla = encontrarpuntosilla(matriz,tamanio)
	print("La matriz tiene ",psilla," puntos de silla en total")
	print("")
