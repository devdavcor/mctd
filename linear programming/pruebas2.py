import numpy as np

num_filas = 3
num_columnas = 4

array_bidimensional = np.zeros((num_filas, num_columnas))

array_bidimensional[2, 1] = 9

print(array_bidimensional)

k = 0
for j in range (3):
	for i in range (4):
		array_bidimensional[j, i] = k
		k += 1
	
print(array_bidimensional)