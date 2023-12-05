from functions import *

# ---------- Variables globales del programa ----------

text_of = "Ingrese el número de variables del modelo, por favor: "
text_r = "Ingrese el número de restricciones del modelo, por favor: "

num_var = is_integer(text_of)
num_restr = is_integer(text_r)


array_objective_function = get_function(num_var)
print_function(array_objective_function)