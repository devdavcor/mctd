from functions import *
import string

print("Trabajando la función objetivo")
array_objective_function = get_objective_function()
print("Trabajando las restricciones")
array_f_restrictions = get_f_restrictions (len(array_objective_function) - 1)
print("Trabajando las combinaciones")
get_f_restrictions_ec_systems(array_f_restrictions, array_objective_function)