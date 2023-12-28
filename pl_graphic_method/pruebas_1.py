from itertools import combinations

# Definir el rango de números

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


rango_numeros = range(len(mi_lista)+1)  # Del 0 al 10
rango_numeros = range(10000)  # Del 0 al 10



# Calcular todas las combinaciones de 2 elementos en el rango
combinaciones = list(combinations(rango_numeros, 2))

# Imprimir las combinaciones
for combinacion in combinaciones:
    print(combinacion)
