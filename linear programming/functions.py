import numpy as np
import string
from itertools import combinations


# ---------- Funciones para obtener la función objetivo ----------
def get_function(num_var):
	# Pide el número de variables de la función objetivo z validando que solo sea entero positivo.
	#num_var = is_integer()
	aux_abc = string.ascii_lowercase
	function_array = np.zeros(num_var)
	for i in range(num_var):
		function_array[i] = is_numeric(aux_abc[i])
	return function_array


def is_integer(text_to_show):
	# The functions validates if the input is an integer
	while True:
		try:
			num_var = int(input(text_to_show))
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
	for i in range(len(function_array)):
		if i > 0 or (i == 0 and get_sign(function_array[i]) != '+'):
			aux_text = str(get_sign(function_array[i])) + " " + str(int(abs(function_array[i]))) + str(aux_abc[i]) + " "
			function_text = function_text + aux_text
		elif i == 0 and get_sign(function_array[i]) == '+':
			aux_text = str(int(abs(function_array[i]))) + str(aux_abc[i]) + " "
			function_text = function_text + aux_text
	print(function_text)
	return


# ---------- Funciones para obtener las restricciones ----------

def get_restriction(num_restr):
	#num_restr = is_integer_restriction()
	array_restrictions = np.zeros(num_restr)
	return print(f"El número de restricciones del modelo es de {num_restr} por lo que el modelo queda {array_restrictions}")

def get_sign(value):
	if value > 0:
		return '+'
	elif value < 0:
		return '-'

# ---------- Funciones para obtener los resultados ----------
#Obtiene las combinaciones posibles para los sistemas de ecuaciones y conocer las intersecciones
def get_combinations(num_restr):
    secuence = range(num_restr)
    combinats = list(combinations(secuence, 2))
    array_index_restriction_combination = np.array(combinats)
    for combina in array_index_restriction_combination:
        print(combina)
    return array_index_restriction_combination

def get_ec_restr_combination(array_restrictions_functions):
	
	return

array_prueba = get_combinations(5)
print(f"El valor del numero que pensé es {array_prueba[5,1]}")
print(f"El valor del numero que pensé es {50*array_prueba[5,1]}")