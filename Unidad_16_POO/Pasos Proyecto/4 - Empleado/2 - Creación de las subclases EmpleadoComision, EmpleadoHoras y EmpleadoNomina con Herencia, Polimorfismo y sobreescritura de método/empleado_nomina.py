# Creación de la subclase "EmpleadoNomina".

"""
Datos de la clase a crear.

    - Nombre Clase: EmpleadoNomina
    - Tipo: Subclase de Empleado
    - Atributos heredados de la superclase Empleado:

        - DNI.
        - Nombre.
        - Apellidos.
        - Email.
        - Especialidad.

    - Atributos propios de la clase EmpleadoNomina:

        - Porcentaje Prestaciones.

    - Método heredado de la superclase Empleado:

        + pro_calcular_salario().
"""

# Se importa la superclase Figura del archivo "empleado.py".
from .empleado import Empleado


# Se crea la subclase "EmpleadoNomina" de la superclase "Empleado".
class EmpleadoNomina(Empleado):

    # Definición del constructor con los atributos heredados y propios.
    def __init__(self, dni, nombre, apellidos, email, especialidad, porcentaje_prestaciones):

        # Se llama al método inicializador de la superclase Empleado.
        super(EmpleadoNomina, self).__init__(dni, nombre, apellidos, email, especialidad)

        # Se crean las variables de instancia de los atributos propios.
        self.a_porcentaje_prestaciones = porcentaje_prestaciones

        # Se crea una variable para indicar que el salario inicial de un empleado por nómina son de 2.000
        self.w_salario_nomina = 2000

    # Se crea el método "pro_calcular_salario()" para calcular el salario de los empleados con comisiones y para ello
    # tenemos que sobreescribir el método "pro_calcular_salario()" de la superclase "Empleado" obteniendo el salario
    # para luego a ese importe, se le suma lo que es al salario multiplicarle 1 menos el porcentaje de prestaciones.
    def pro_calcular_salario(self):

        w_total_salario = super(EmpleadoNomina, self).pro_calcular_salario() + (self.w_salario_nomina * (1 - self.a_porcentaje_prestaciones))
        return w_total_salario
