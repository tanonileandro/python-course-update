
'''
# Funcion para ,mandar un saludo
def greet():
   name = input('Ingrese su nombre: ')
   print(f'Buenas tardes {name}, espero que te encuentres bien.')'''

# Ejemplo pasando paremetros
def sum(value1, value2):
   result = value1 + value2
   return result

def new_person(name, surname, age):
   print(f'''
         Nueva persona:
            Nombre: {name}
            Apellido: {surname}
            Edad: {age}
         ''')


if __name__ == '__main__': 
   # Para que no se impriman las demas funciones en otras importaciones
   # Solo esta funcion se va a ejecutar cuando se ejecute este archivo

   print('*** Funciones en Python ***')
   # Llamamos la funcion, en python las mismas con objetos
  
   # greet()

   person = new_person('Leandro', 'Tanoni', 28)
   person2 = new_person(name='Leandro', surname='Tanoni', age=28)
   person3 = new_person(surname='Tanoni', age=28, name='Leandro') # Declarando por nombre podemos alterar el orden en que ingresamos los datos