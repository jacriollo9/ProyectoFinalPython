import numpy

def comprobarprimo(num):
        cont = 0
        for i in range(1, num+1):
            if (num % i == 0):
                cont += 1
        if (cont == 2):
            return True
        else:
            return False
        

matrizA = numpy.zeros([4, 6],dtype=int)
matrizB = numpy.zeros([4, 6],dtype=int)
primoMayor = 0
repetidor = 0

print(("Ingresar los valores de la matriz A"))
for i in range(0,4,1):
	for j in range(0,6,1):
		print("Ingresar el elemento matrizA:  [ ",i,"] [",j,"]: " , end="")
		matrizA[i][j] = input()

print(("Ingresar los valores de la matriz B"))
for i in range(0,4,1):
	for j in range(0,6,1):
		print("Ingresar el elemento matrizB [ ",i,"] [",j,"]: ", end="")
		matrizB[i][j] = input()


print("MATRIZ A")
for i in range(0,4,1):
	print("")
	for j in range(0,6,1):
		print(matrizA[i][j],"  ", end="")
print(" ")

print("MATRIZ B")
for i in range(0,4,1):
	print("")
	for j in range(0,6,1):
		print(matrizB[i][j],"  ", end="")
print(" ")

for i in range (0, 4):
    for j in range (0, 6): 
        if (comprobarprimo(matrizA[i][j])):
            mayor=matrizA[i][j]
            for k in range(0, 4):
                for l in range(0, 6):
                    actual=matrizA[k][l]
                    if (comprobarprimo(actual)):
                        if (actual > mayor):
                            mayor=actual    
            primoMayor=mayor
                
for i in range(0, 4):
    for j in range(0, 6):      
        if primoMayor == matrizB[i][j]:
            repetidor = repetidor + 1

print(f"El numero primo {primoMayor} de la primera matriz se repite {repetidor} en la segunda matriz.")