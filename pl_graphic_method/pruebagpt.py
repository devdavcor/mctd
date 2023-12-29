from itertools import combinations
import numpy as np


def get_f_restrictions_combinations(num_restrictions, num_variables):
	array_f_restrictions_combinations_index = list(combinations(range(num_restrictions), num_variables))
	for sys_ec in array_f_restrictions_combinations_index:
		print(sys_ec)
	return array_f_restrictions_combinations_index


def get_f_restrictions_ec_systems(array_f_restrictions, array_f_restrictions_combinations_index):
	array_f_restrictions_ec_systems = list(combinations(range(num_restrictions), num_variables))
	row, columns = len(array_f_restrictions_ec_systems), len(array_f_restrictions_ec_systems[0])
	for i in range(row):
		current_row = []  # Nueva línea para almacenar temporalmente los valores en una lista
		for j in range(columns):
			aux = array_f_restrictions_ec_systems[i][j]
			aux_2 = array_f_restrictions[aux]
			current_row.append(aux_2)  # Almacena el valor en la lista temporal
			print(f"El valor en [{i}][{j}] es: {current_row[j]}")
		array_f_restrictions_ec_systems[i] = tuple(current_row)  # Convierte la lista a tupla antes de asignarla
	return array_f_restrictions_ec_systems


mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alfabeto = ['a', 'b', 'c', 'd', 'e']
num_restrictions = len(alfabeto)
num_variables = 2

array_prueba = get_f_restrictions_combinations(num_restrictions, num_variables)

get_f_restrictions_ec_systems(alfabeto, array_prueba)
