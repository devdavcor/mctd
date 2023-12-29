import numpy as np
import string
from itertools import combinations

# ----------------------    Global variables    ----------------------
alfabet = list(string.ascii_uppercase)


# ----------------------    Auxiliar functions    ----------------------
def is_number(text):
	while True:
		number = input(text)
		try:
			number = float(number)
			return number  # Return the number
		except ValueError:
			print("Error. Try again.")


def is_positive_integer(text):
	while True:
		number = input(text)
		try:
			number = int(number)
			if number > 0:
				return number  # Return the number if it's a positive integer
			else:
				print("Error. The number must be a positive integer.")
		except ValueError:
			print("Error. Try again.")
			



# ----------------------    To print functions    ----------------------

def print_function(array_function):
	text_function = ''
	for coefficient in range(len(array_function)):
		if coefficient == len(array_function) - 1:
			text_aux = ' = ' + (' + ' if array_function[coefficient] >= 0 else ' - ') + str(
				int(abs(array_function[coefficient])))
			text_function += text_aux
		else:
			text_aux = (' + ' if array_function[coefficient] >= 0 else ' - ') + str(
				int(abs(array_function[coefficient]))) + alfabet[coefficient]
			text_function += text_aux
	print(text_function)
	return



# ----------------------    To get information functions    ----------------------
def get_objective_function():
	number_variables = int(is_positive_integer("Please, get the numbers of variables in objective functions:"))
	array_objective_function = np.zeros(number_variables + 1)
	for coefficient in range(len(array_objective_function)):
		if coefficient == len(array_objective_function) - 1:
			array_objective_function[coefficient] = is_number(f"Please, get the coefficent of the independent term:")
		else:
			array_objective_function[coefficient] = is_number(
				f"Please, get the coefficent of the variable {alfabet[coefficient]}: ")
	print_function(array_objective_function)
	return array_objective_function


def get_f_restrictions(var_number):
	num_restrictions = int(is_positive_integer("Please, get the numbers of restrictions for the model:"))
	array_f_restrictions = np.zeros((num_restrictions, var_number + 1))
	restrictions, coefficients = array_f_restrictions.shape
	for restriction in range(restrictions):
		for coefficient in range(coefficients):
			if coefficient == coefficients - 1:
				array_f_restrictions[restriction, coefficient] = is_number(
					f"Please, get the coefficent of the independent term:")
			else:
				array_f_restrictions[restriction, coefficient] = is_number(
					f"Please, get the coefficent of the variable {alfabet[coefficient]}: ")
	for restriction in array_f_restrictions:
		print_function(restriction)
	# print(array_f_restrictions)
	return array_f_restrictions

def get_f_restrictions_ec_systems(array_f_restrictions):
	array_f_restrictions_ec_systems = list(combinations(range(num_restrictions), num_variables))
	row, columns = len(array_f_restrictions_ec_systems), len(array_f_restrictions_ec_systems[0])
	for i in range(row):
		current_row = []
		for j in range(columns):
			aux = array_f_restrictions_ec_systems[i][j]
			aux_2 = array_f_restrictions[aux]
			current_row.append(aux_2)
			print(f"El valor en [{i}][{j}] es: {current_row[j]}")
		array_f_restrictions_ec_systems[i] = tuple(current_row)
	return array_f_restrictions_ec_systems