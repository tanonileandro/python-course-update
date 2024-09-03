# Regresar una tupla de valores desde una funcion aplicando unpacking

# Ejemplo 1
def uppercase_person(name, surname, age):
   print('Se devuelve una tupla de valores desde la funcion.')
   return name.upper(), surname.upper(), age

# Ejemplo 2
def coordinates():
   x, y, z = 10, 20, 30
   return x, y, z


# Programa principal 

print('Ejemplo 1')
name, surname, age = uppercase_person('Leandro', 'Tanoni', 28)
print(f'''Resultado persona: 
    Nombre = {name}
    Apellido = {surname}
    Edad = {age}''')


print('\nEjemplo 2')
result = coordinates()
print(result) # Imprimimos la tupla de valores

# Aplicamos unpacking
x1, y1, z1 = result
print(f'Cordenadas: x={x1} y={y1} z={z1}')