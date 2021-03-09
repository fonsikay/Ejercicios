# Se importan las subclases de Empleado.
from clases.empleado_comision import EmpleadoComision
from clases.empleado_horas import EmpleadoHoras
from clases.empleado_nomina import EmpleadoNomina


# Se crea el método principal "app_principal()".
def app_principal():

    # Se crea un objeto de cada una de las subclases de Empleado.
    w_empleado_comision = EmpleadoComision('11111111P', 'Jorge', 'Pérez', 'jorge@gmail.com',
                                           'Informático', 0.30, 10000)

    w_empleado_horas = EmpleadoHoras('22222222G', 'Viviana', 'García', 'viviana@gmail.com', 'Fotografía', 80, 100)
    w_empleado_nomina = EmpleadoNomina('33333333B', 'Patricia', 'Toledo', 'patricia@gmail.com', 'Diseño Gráfico', 0.10)

    # Se crea una lista almacenando los objetos creados de tipo Empleado.
    w_lista_empleados = [w_empleado_comision, w_empleado_horas, w_empleado_nomina]

    print('--------- DATOS DE LOS EMPLEADOS ---------')
    # Se recorre la lista para mostrar por pantalla los datos comunes de los objetos de las subclases de Empleado.
    for r_lista_empleados in w_lista_empleados:

        print('\nLos datos del tipo {} son:\n'.format(type(r_lista_empleados).__name__))
        print('- DNI: {}'.format(r_lista_empleados.a_dni))
        print('- Nombre: {}'.format(r_lista_empleados.a_nombre))
        print('- Apellidos: {}'.format(r_lista_empleados.a_apellidos))
        print('- Email: {}'.format(r_lista_empleados.a_email))
        print('- Especialidad: {}'.format(r_lista_empleados.a_especialidad))
        print('- Salario: {}'.format(r_lista_empleados.pro_calcular_salario()))


# Se comprueba si se está ejecutando el método "main", ejecuta nuestro método "app_principal()".
if __name__ == '__main__':
    app_principal()
