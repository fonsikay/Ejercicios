# Creación de la clase "EmpleadoComision".

"""
Datos de la clase a crear.

    - Nombre Clase: EmpleadoComision
    - Tipo: Subclase de Empleado
    - Atributos heredados de la superclase Empleado:

        - DNI.
        - Nombre.
        - Apellidos.
        - Email.
        - Especialidad.

    - Atributos propios de la clase EmpleadoComision:

        - Porcentaje Comision.
        - Monto.

    - Método heredado de la superclase Empleado:

        + pro_calcular_salario().
"""

# Se importa la superclase Figura del archivo "empleado.py".
from .empleado import Empleado


# Se crea la subclase "EmpleadoComision" de la superclase "Empleado".
class EmpleadoComision(Empleado):

    # Definición del constructor con los atributos heredados y propios.
    def __init__(self, dni, nombre, apellidos, email, especialidad, porcentaje_comision, monto):

        # Se llama al método inicializador de la superclase Empleado.
        super(EmpleadoComision, self).__init__(dni, nombre, apellidos, email, especialidad)

        # Se crean las variables de instancia de los atributos propios.
        self.a_porcentaje_comision = porcentaje_comision
        self.a_monto = monto

    # Se crea el método "pro_calcular_salario()" para calcular el salario de los empleados con comisiones y para ello
    # tenemos que sobreescribir el método "pro_calcular_salario()" de la superclase "Empleado" obteniendo el salario
    # para luego a ese importe, sumarle el monto por el porcentaje de comisión.
    def pro_calcular_salario(self):

        w_total_salario = super(EmpleadoComision, self).pro_calcular_salario() + (self.a_monto * self.a_porcentaje_comision)
        return w_total_salario
