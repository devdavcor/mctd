from itertools import combinations

n=10
# Definir la secuencia de números
secuencia = range(n+1)  # Asegúrate de incluir n en la secuencia

# Calcular las combinaciones en grupos de 2
combinaciones = combinations(secuencia, 2)

# Mostrar las combinaciones
for combinacion in combinaciones:
    print(combinacion)
