import numpy as np
import string
def get_function():
	#Pide el número de variables de la función objetivo z validando que solo sea entero positivo.
	num_var = is_integer()
	aux_abc = string.ascii_lowercase
	function_array = np.zeros(num_var)
	for i in range (num_var):
		function_array[i] = is_numeric(aux_abc[i])
	return function_array

def is_integer ():
#The functions validates if the input is an integer
	while True:
		try:
			num_var = int(input("Ingrese el número de variables de la ecuación, por favor: "))
			if num_var > 0:
				break
			else:
				print("Por favor, ingrese un número entero positivo.")
		except ValueError:
			print("Por favor, ingrese un número entero válido.")
	return num_var

def is_numeric(variable_letter):
    # La función valida si el input es un número
    while True:
        try:
            num_var = float(input(f'Ingrese coeficiente para la variable {variable_letter}'))
            break  # Romper el bucle cuando se ingresa un número válido
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return num_var

def print_function(function_array):
	function_text = "La función objetivo z = "
	aux_abc = string.ascii_lowercase
	for i in range (len(function_array)):
		if i > 0 or (i == 0 and get_sign(function_array[i]) != '+'):
			aux_text = str(get_sign(function_array[i])) + " " + str(int(abs(function_array[i]))) + str(aux_abc[i]) + " "
			function_text = function_text + aux_text
		elif i == 0 and get_sign(function_array[i]) == '+':
			aux_text = str(int(abs(function_array[i]))) + str(aux_abc[i]) + " "
			function_text = function_text + aux_text
	print(function_text)
	return

def get_sign(value):
    if value > 0:
        return '+'
    elif value < 0:
        return '-'
    

print_function(get_function())