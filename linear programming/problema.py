import numpy as np

# Crear un array de 10x2 con letras que no se repiten
letras = np.random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), size=(10, 2), replace=False)

print("Array de 10x2 con letras que no se repiten:")
print(letras)
