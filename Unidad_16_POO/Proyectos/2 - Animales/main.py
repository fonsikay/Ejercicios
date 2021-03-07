# Creación de objetos o instanciación.

# Se importan las subclases Gato, Pato y Perro.
from clases.gato import Gato
from clases.pato import Pato
from clases.perro import Perro


# Se crea el método "app_principal()".
def app_principal():

    # Se crea una lista vacia para luego almacenar los objetos creados.
    w_lista_animales = []

    # Se crea un objeto de la clase "Pato".
    w_pato = Pato('Lucas', 2, 'Anas platyrhynchos domesticus', 'Verde')

    # Se crea un objeto de la clase "Gato".
    w_gato = Gato('Luna', 1, 'Felis catus', True)

    # Se crea un objeto de la clase "Perro".
    w_perro = Perro('Crisposo', 2, 'Canis lupus familiaris', 'Rotwailer')

    # Se agregan los objetos de los animales a la lista de animales.
    w_lista_animales.append(w_pato)
    w_lista_animales.append(w_gato)
    w_lista_animales.append(w_perro)

    # Se recorre la lista de animales para obtener los datos de los atributos que tienen en común los objetos creados
    # y se lanzan también los métodos comunes incluido el método abstracto "pro_hablar()".
    for r_lista_animales in w_lista_animales:

        print('\n------ DATOS DEL ANIMAL {} ------\n'.format(type(r_lista_animales).__name__).upper())
        print('- Nombre: {}'.format(r_lista_animales.a_nombre))
        print('- Edad: {}'.format(r_lista_animales.a_edad))
        print('- Nombre científico: {}'.format(r_lista_animales.a_nombre_cientifico))
        r_lista_animales.pro_comer()
        r_lista_animales.pro_moverse()

    print('\nEl cuidador del zoológico les dice a todos los animales que hablen ahora:\n')

    for r_lista_animales in w_lista_animales:
        r_lista_animales.pro_hablar()


# Si se ejecuta el archivo "main.py", se lanza el método "main()".
if __name__ == '__main__':
    app_principal()
