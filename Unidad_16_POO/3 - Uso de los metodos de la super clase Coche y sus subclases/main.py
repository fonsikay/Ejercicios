# Creación de objetos o instanciación.

# Se importa la clase "Coche" creada en el archivo "coche.py".
from modelos.coche import Coche
# Se importa la clase "Camión" creada en el archivo "camion.py".
from modelos.camion import Camion
# Se importa la clase "Deportivo" creada en el archivo "deportivo.py".
from modelos.deportivo import Deportivo
# Se importa la clase "Camioneta" creada en el archivo "camioneta.py".
from modelos.camioneta import Camioneta
# Se importa la clase "Formula 1" creada en el archivo "formula1.py".
from modelos.formula1 import Formula1


# Se crea un método para iniciar la creación de los objetos necesarios.
def app_principal():

    # CREACION Y USO DE UN OBJETO DE LA CLASE COCHE --------------------------------------------------------------------

    # Se crea un objeto de la clase Coche para el coche Seat Ibiza
    w_seat_ibiza = Coche('8676FNR', 'Seat', 'Ibiza', 'España')

    print('----------- DATOS DE LA CLASE COCHE -----------\n')

    # Se obtiene el nombre del paquete, subpaquete y clase del objeto.
    print('El tipo de dato de la variable "w_seat_ibiza" es: {}'.format(type(w_seat_ibiza)))
    # Se obtiene el nombre de la clase del objeto.
    print('El nombre de la clase de la variable "w_seat_ibiza" es: {}'.format(type(w_seat_ibiza).__name__))

    # Se obtiene el valor de los atributos de la clase "Coche" indicadas en la creación.
    print('\nLos datos del nuevo coche son:\n')
    print('- Matrícula: {}'.format(w_seat_ibiza.a_matricula))
    print('- Marca: {}'.format(w_seat_ibiza.a_marca))
    print('- Modelo: {}'.format(w_seat_ibiza.a_modelo))
    print('- País de procedencia: {}'.format(w_seat_ibiza.a_pais_procedencia))
    # Se indica que si el valor es True, indique un 'Si' y si el valor es False, pues que indique 'No'.
    print('- ¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.a_estado else 'No'))

    # Se llama a los métodos de la clase "Coche".

    print('\nSe lanzan los métodos de instancia de la clase "Coche".\n')
    w_seat_ibiza.pro_apagar()
    w_seat_ibiza.pro_encender()
    print('¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.a_estado else 'No'))
    w_seat_ibiza.pro_apagar()
    print('¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.a_estado else 'No'))
    w_seat_ibiza.pro_acelerar()
    w_seat_ibiza.pro_encender()
    w_seat_ibiza.pro_acelerar()
    w_seat_ibiza.pro_frenar()
    w_seat_ibiza.pro_frenar()
    w_seat_ibiza.pro_encender()
    w_seat_ibiza.pro_apagar()
    print('¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.a_estado else 'No'))

    # CREACION Y USO DE UN OBJETO DE LA CLASE CAMION -------------------------------------------------------------------

    w_camion_carga = Camion('9010BD', 'Mercedes', 'Benz', 'Alemania', 45000)

    print('\n ----------- DATOS DE LA CLASE CAMIÓN -----------\n')
    print('El tipo de dato de la variable "w_camion_carga" es: {}'.format(type(w_camion_carga)))
    print('El tipo de dato de la variable "w_camion_carga" es: {}'.format(type(w_camion_carga).__name__))

    # Se obtiene el valor de todos los atributos de la clase "Camion" indicadas en la creación.
    print('\nLos datos del nuevo camión son:\n')
    print('- Matrícula: {}'.format(w_camion_carga.a_matricula))
    print('- Marca: {}'.format(w_camion_carga.a_marca))
    print('- Modelo: {}'.format(w_camion_carga.a_modelo))
    print('- Pais de procedencia: {}'.format(w_camion_carga.a_pais_procedencia))
    print('- Capacidad de carga (kg): {}'.format(w_camion_carga.a_capacidad_carga))
    print('- ¿El camión está encendido?: {}'.format('Si' if w_camion_carga.a_estado else 'No'))

    # Se llama a los métodos de la clase "Coche" y de la clase "Camión".
    print('\nSe lanzan los métodos de instancia de la clase "Camión".\n')

    w_camion_carga.pro_encender()
    print('- ¿El camión está encendido?: {}'.format('Si' if w_camion_carga.a_estado else 'No'))
    w_camion_carga.pro_acelerar()
    w_camion_carga.pro_frenar()
    w_camion_carga.pro_cargar_mercancia()
    w_camion_carga.pro_acelerar()
    w_camion_carga.pro_frenar()
    w_camion_carga.pro_descargar_mercancia()
    w_camion_carga.pro_apagar()
    print('- ¿El camión está encendido?: {}'.format('Si' if w_camion_carga.a_estado else 'No'))

    # CREACION Y USO DE UN OBJETO DE LA CLASE DEPORTIVO ----------------------------------------------------------------

    w_ferrari = Deportivo('1547LHN', 'Ferrari', '488 GTB Spider', 'Italia', 'Llantas Ferrari Original', 'Hiper-Deportivo')

    print('\n ----------- DATOS DE LA CLASE DEPORTIVO -----------\n')
    print('El tipo de dato de la variable "w_ferrari" es: {}'.format(type(w_ferrari)))
    print('El tipo de dato de la variable "w_ferrari" es: {}'.format(type(w_ferrari).__name__))

    # Se obtiene el valor de todos los atributos de la clase "Deportivo" indicadas en la creación.
    print('\nLos datos del nuevo deportivo son:\n')
    print('- Matrícula: {}'.format(w_ferrari.a_matricula))
    print('- Marca: {}'.format(w_ferrari.a_marca))
    print('- Modelo: {}'.format(w_ferrari.a_modelo))
    print('- Pais de procedencia: {}'.format(w_ferrari.a_pais_procedencia))
    print('- Marca de llantas: {}'.format(w_ferrari.a_marca_llantas))
    print('- Tipo de deportivo: {}'.format(w_ferrari.a_tipo_deportivo))
    print('- ¿El deportivo está encendido?: {}'.format('Si' if w_ferrari.a_estado else 'No'))

    # Se llama a los métodos de la clase "Coche" y de la clase "Deportivo".
    print('\nSe lanzan los métodos de instancia de la clase "Deportivo".\n')
    w_ferrari.pro_abrir_puertas()
    w_ferrari.pro_cerrar_puertas()
    w_ferrari.pro_encender()
    print('- ¿El deportivo está encendido?: {}'.format('Si' if w_ferrari.a_estado else 'No'))
    w_ferrari.pro_acelerar()
    w_ferrari.pro_frenar()
    w_ferrari.pro_apagar()
    print('- ¿El deportivo está encendido?: {}'.format('Si' if w_ferrari.a_estado else 'No'))
    w_ferrari.pro_abrir_puertas()
    w_ferrari.pro_cerrar_puertas()

    # CREACION Y USO DE UN OBJETO DE LA CLASE CAMIONETA ----------------------------------------------------------------

    w_camioneta = Camioneta('4752HRF', 'Chevrolet', 'Colorado 2021', 'Estados Unidos', 25000, 1256.50)

    print('\n ----------- DATOS DE LA CLASE CAMIONETA -----------\n')
    print('El tipo de dato de la variable "w_camioneta" es: {}'.format(type(w_camioneta)))
    print('El tipo de dato de la variable "w_camioneta" es: {}'.format(type(w_camioneta).__name__))

    # Se obtiene el valor de todos los atributos de la clase "Camioneta" indicadas en la creación.
    print('\nLos datos de la nueva camioneta son:\n')
    print('- Matrícula: {}'.format(w_camioneta.a_matricula))
    print('- Marca: {}'.format(w_camioneta.a_marca))
    print('- Modelo: {}'.format(w_camioneta.a_modelo))
    print('- Pais de procedencia: {}'.format(w_camioneta.a_pais_procedencia))
    print('- Capacidad de carga: {}'.format(w_camioneta.a_capacidad_carga))
    print('- Precio del servicio: {}'.format(w_camioneta.a_costo_servicio))
    print('- ¿La camioneta está encendida?: {}'.format('Si' if w_camioneta.a_estado else 'No'))

    # Se llama a los métodos de la clase "Coche" y de la clase "Camioneta".
    print('\nSe lanzan los métodos de instancia de la clase "Camioneta".\n')
    w_camioneta.pro_encender()
    print('- ¿La camioneta está encendida?: {}'.format('Si' if w_camioneta.a_estado else 'No'))
    w_camioneta.pro_acelerar()
    w_camioneta.pro_frenar()
    w_camioneta.pro_cargar_material()
    w_camioneta.pro_acelerar()
    w_camioneta.pro_frenar()
    w_camioneta.pro_descargar_material()
    w_camioneta.pro_apagar()
    print('- ¿La camioneta está encendida?: {}'.format('Si' if w_camioneta.a_estado else 'No'))

    # CREACION Y USO DE UN OBJETO DE LA CLASE FORMULA1 -----------------------------------------------------------------

    w_renault_f1 = Formula1('RNT-F1', 'Renault', 'Alpine A521 F1', 'Francia', 10000)

    print('\n ----------- DATOS DE LA CLASE FORMULA 1 -----------\n')
    print('El tipo de dato de la variable "w_renault_f1" es: {}'.format(type(w_renault_f1)))
    print('El tipo de dato de la variable "w_renault_f1" es: {}'.format(type(w_renault_f1).__name__))

    # Se obtiene el valor de todos los atributos de la clase "Camioneta" indicadas en la creación.
    print('\nLos datos del nuevo Formula 1 son:\n')
    print('- Matrícula: {}'.format(w_renault_f1.a_matricula))
    print('- Marca: {}'.format(w_renault_f1.a_marca))
    print('- Modelo: {}'.format(w_renault_f1.a_modelo))
    print('- Pais de procedencia: {}'.format(w_renault_f1.a_pais_procedencia))
    print('- Peso: {}'.format(w_renault_f1.a_peso))
    print('- ¿El Formula 1 está encendido?: {}'.format('Si' if w_renault_f1.a_estado else 'No'))

    # Se llama a los métodos de la clase "Coche" y de la clase "Formula1".
    print('\nSe lanzan los métodos de instancia de la clase "Formula1".\n')
    w_renault_f1.pro_encender()
    print('- ¿El Formula 1 está encendido?: {}'.format('Si' if w_renault_f1.a_estado else 'No'))
    w_renault_f1.pro_competir()
    w_renault_f1.pro_acelerar()
    w_renault_f1.pro_acelerar()
    w_renault_f1.pro_acelerar()
    w_renault_f1.pro_frenar()
    w_renault_f1.pro_apagar()
    print('- ¿El Formula 1 está encendido?: {}'.format('Si' if w_renault_f1.a_estado else 'No'))


# Se ejecuta el método principal de la aplicación.
if __name__ == '__main__':
    app_principal()
