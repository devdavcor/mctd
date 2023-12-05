import numpy as np

# Coeficientes de las ecuaciones
coefficients = np.array([[2, 3], [1, -2]])

# Términos independientes
constants = np.array([8, -1])

# Verificar si la matriz de coeficientes es singular
if np.linalg.det(coefficients) == 0:
    print("El sistema no tiene solución única.")
else:
    # Resolver el sistema de ecuaciones
    solution = np.linalg.solve(coefficients, constants)
    print("La solución del sistema es:", solution)
