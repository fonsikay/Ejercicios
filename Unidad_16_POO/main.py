# Creación de objetos o instanciación.

# Se importa la clase "Coche" creada en el archivo "Coche.py".
from modelos.coche import Coche


# Se crea un método para iniciar la creación de los objetos necesarios.
def main():
    
    # Se crea un objeto de la clase Coche para el coche Seat Ibiza
    w_seat_ibiza = Coche('8676FNR', 'Seat', 'Ibiza', 'España')

    # Se obtiene el nombre del paquete, subpaquete y clase del objeto.
    print('El tipo de dato de la variable coche es: {}'.format(type(w_seat_ibiza)))
    # Se obtiene el nombre de la clase del objeto.
    print('El tipo de dato de la variable coche es: {}'.format(type(w_seat_ibiza).__name__))

    # Se obtiene el valor de los atributos de la clase "Coche" indicadas en la creación.
    print('\nLos datos del nuevo coche son:\n')
    print('- Matrícula: {}'.format(w_seat_ibiza.pe_matricula))
    print('- Marca: {}'.format(w_seat_ibiza.pe_marca))
    print('- Modelo: {}'.format(w_seat_ibiza.pe_modelo))
    print('- País de procedencia: {}'.format(w_seat_ibiza.pe_pais_procedencia))
    print('- Estado: {}'.format(w_seat_ibiza.w_estado))


# Se ejecuta el método principal de la aplicación.
if __name__ == '__main__':
    main()