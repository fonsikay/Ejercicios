# Creación de objetos o instanciación.

# Se importa la clase "Coche" creada en el archivo "Coche.py".
from modelos.coche import Coche


# Se crea un método para iniciar la creación de los objetos necesarios.
def app_principal():
    
    # Se crea un objeto de la clase Coche para el coche Seat Ibiza
    w_seat_ibiza = Coche('8676FNR', 'Seat', 'Ibiza', 'España')

    # Se obtiene el nombre del paquete, subpaquete y clase del objeto.
    print('El tipo de dato de la variable coche es: {}'.format(type(w_seat_ibiza)))
    # Se obtiene el nombre de la clase del objeto.
    print('El tipo de dato de la variable coche es: {}'.format(type(w_seat_ibiza).__name__))

    # Se obtiene el valor de los atributos de la clase "Coche" indicadas en la creación.
    print('\nLos datos del nuevo coche son:\n')
    print('- Matrícula: {}'.format(w_seat_ibiza.a_matricula))
    print('- Marca: {}'.format(w_seat_ibiza.a_marca))
    print('- Modelo: {}'.format(w_seat_ibiza.a_modelo))
    print('- País de procedencia: {}'.format(w_seat_ibiza.a_pais_procedencia))
    # Se indica que si el valor es True, indique un 'Si' y si el valor es False, pues que indique 'No'.
    print('- ¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.w_estado else 'No'))

    # Se llama a los métodos de la clase "Coche" para cambiar el valor del atributo "estado".

    print('\nSe lanzan los métodos de instancia.\n')
    w_seat_ibiza.pro_apagar()
    w_seat_ibiza.pro_encender()
    print('¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.w_estado else 'No'))
    w_seat_ibiza.pro_apagar()
    print('¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.w_estado else 'No'))
    w_seat_ibiza.pro_acelerar()
    w_seat_ibiza.pro_encender()
    w_seat_ibiza.pro_acelerar()
    w_seat_ibiza.pro_frenar()
    w_seat_ibiza.pro_frenar()
    w_seat_ibiza.pro_encender()
    w_seat_ibiza.pro_apagar()
    print('¿Está encendido el coche?: {}'.format('Si' if w_seat_ibiza.w_estado else 'No'))


# Se ejecuta el método principal de la aplicación.
if __name__ == '__main__':
    app_principal()