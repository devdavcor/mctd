import matplotlib.pyplot as plt

# Coordenadas de los dos puntos (x1, y1) y (x2, y2)
x1, y1 = 1, 2
x2, y2 = 4, 6

# Calcular la pendiente (m) y la ordenada al origen (b) de la recta
m = (y2 - y1) / (x2 - x1)
b = y1 - m * x1

# Generar puntos para la recta
x_values = [x1, x2]
y_values = [y1, y2]

# Graficar la recta
plt.plot(x_values, y_values, label=f'Recta: y = {m}x + {b}')

# Marcar los puntos
plt.scatter([x1, x2], [y1, y2], color='red', label='Puntos')

# Etiquetas y leyenda
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Mostrar el gráfico
plt.show()
