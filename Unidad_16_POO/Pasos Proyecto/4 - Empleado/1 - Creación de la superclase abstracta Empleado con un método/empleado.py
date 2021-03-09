# Creación de la superclase Empleado.

"""
Datos de la clase a crear.

    - Nombre Clase: Empleado
    - Tipo: Superclase Abstracta

    - Atributos propios de la clase:

        - DNI.
        - Nombre.
        - Apellidos.
        - Email.
        - Especialidad.

    - Métodos propios de la clase:

        + pro_calcular_salario()
"""

# Se importa la libreria "abc" para poder indicar la clase y los métodos como abstractos.
from abc import ABC


# Se crea la clase abstracta "Empleado".
class Empleado(ABC):

    # Se crea una variable estática de clase para almacenar el salario base que van a tener todos los empleados sean
    # del tipo que sean por lo que este tipo de variable hace que se pueda utilizar en todas las subclases que hereden
    # de esta superclase y se escribe con mayúsculas fuera del método "__init__()" de la superclase.
    W_SALARIO_BASE = 1000

    # Definición del constructor con los atributos.
    def __init__(self, dni, nombre, apellidos, email, especialidad):

        # Se crean las variables de instancia de los atributos de la clase.
        self.a_dni = dni
        self.a_nombre = nombre
        self.a_apellidos = apellidos
        self.a_email = email
        self.a_especialidad = especialidad

    # Se crea el método "pro_calcular_salario()" para calcular indicar que el salario total de la clase Empleado es
    # el importe del salario base mas el 10%.
    def pro_calcular_salario(self):

        w_salario_total = Empleado.W_SALARIO_BASE * 1.10
        return w_salario_total
