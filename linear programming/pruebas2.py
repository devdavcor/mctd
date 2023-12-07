import numpy as np

# Crear un array bidimensional con letras del alfabeto
letras_alfabeto_bidimensional = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
letras_alfabeto_bidimensional_2 = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")).reshape(13, 2)

print(letras_alfabeto_bidimensional_2)

for i in range (13):
	for j in range (2):
		print(f"El valor del array en [{i},{j}] es {letras_alfabeto_bidimensional_2[i,j]}")
		
array_numeros = np.arange(26)
np.random.shuffle(array_numeros)
array_bidimensional = array_numeros.reshape((13, 2))

#np.random.shuffle(array_numeros)
array_bidimensional = array_numeros.reshape((13, 2))

print(array_bidimensional)

array_aux = []

for i in range (13):
	for j in range (2):
		aux = array_bidimensional[i, j]
		#array_ceros[i, j] = letras_alfabeto_bidimensional[array_bidimensional[i, j]]
		array_aux.append(letras_alfabeto_bidimensional[aux])
		print(f"El valor del array es {letras_alfabeto_bidimensional[aux]}")

print(array_aux)
array_original = np.array(array_aux)

# Reformatear a un array de 13x2
array_13x2 = array_original.reshape((13, 2))

print(array_13x2)