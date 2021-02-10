def comprobardigito(num, digito):
	res = bool()
	if (num%10==digito):
		res = True
	return res

if __name__ == '__main__':
	long = int()
	contador = int()
	digito = int()
	i = int()
	vector = int()
	terminaen = bool()
	vector = [int() for ind0 in range(10)]
	print("Ingrese el dígito a analizar: ")
	digito = int(input())
	contador = 0
	terminaen = False
	print("Ingrese los valores del vector: ")
	for i in range(1,11):
		print("Ingrese el ",i," valor")
		vector[i-1] = int(input())
		if comprobardigito(vector[i-1],digito):
			contador = contador+1
	print("El digito ",digito," se repite ",contador," veces en el vector, en las posiciones: ")
	for i in range(1,11):
		if comprobardigito(vector[i-1],digito):
			print(i," , ", end="")

