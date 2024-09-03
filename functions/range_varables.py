# Alcance de variables (Locales y globales)

# Vroable global
global_counter = 0

def increment_counter():
   # Variable local
   local_counter = 0
   # Llamar a la variable global
   global global_counter

   # Incrementar variables
   local_counter += 1
   global_counter += 1

   print(f'''
Contador local: {local_counter}
Contador global: {global_counter}
''')
   
increment_counter()
increment_counter()
increment_counter()

# La variable global a medida que se ejecute mas veces va a incrementar, mientras que la otra va a resetearse en cada ejecucion