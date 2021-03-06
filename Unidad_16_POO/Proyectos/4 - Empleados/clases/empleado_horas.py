# Creación de la subclase "EmpleadoHoras".

"""
Datos de la clase a crear.

    - Nombre Clase: EmpleadoHoras
    - Tipo: Subclase de Empleado
    - Atributos heredados de la superclase Empleado:

        - DNI.
        - Nombre.
        - Apellidos.
        - Email.
        - Especialidad.

    - Atributos propios de la clase EmpleadoHoras:

        - Numero Horas.
        - Precio Horas.

    - Método heredado de la superclase Empleado:

        + pro_calcular_salario().
"""

# Se importa la superclase Figura del archivo "empleado.py".
from .empleado import Empleado


# Se crea la subclase "EmpleadoHoras" de la superclase "Empleado".
class EmpleadoHoras(Empleado):

    # Definición del constructor con los atributos heredados y propios.
    def __init__(self, dni, nombre, apellidos, email, especialidad, numero_horas, precio_horas):

        # Se llama al método inicializador de la superclase Empleado.
        super(EmpleadoHoras, self).__init__(dni, nombre, apellidos, email, especialidad)

        # Se crean las variables de instancia de los atributos propios.
        self.a_numero_horas = numero_horas
        self.a_precio_horas = precio_horas

    # Se crea el método "pro_calcular_salario()" para calcular el salario de los empleados con comisiones y para ello
    # tenemos que sobreescribir el método "pro_calcular_salario()" de la superclase "Empleado" obteniendo el salario
    # para luego a ese importe, sumarle el producto entre el numero de horas y el precio de hora.
    def pro_calcular_salario(self):

        w_total_salario = super(EmpleadoHoras, self).pro_calcular_salario() + (self.a_numero_horas * self.a_precio_horas)
        return w_total_salario
