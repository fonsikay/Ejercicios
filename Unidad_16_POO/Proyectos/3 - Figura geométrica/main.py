# Se importa las clases de las figuras a crear.
from clases.rectangulo import Rectangulo
from clases.circulo import Circulo
from clases.triangulo import Triangulo


# Se crea el método principal llamado "main".
def app_principal():

    # Prueba de ejecución sobre la jerarquía de herencia de "Figuras" con Polimorfísmo.

    # Se crea una lista vacía para almacenar los objetos de las subclases de Figura.
    w_lista_figuras = []

    # Se crea un objeto de la clase "Rectángulo".
    w_rectangulo = Rectangulo('Amarillo', 'Azul', 50, 20)
    # Se crea un objeto de la clase "Circulo".
    w_circulo = Circulo('Rojo', 'Amarillo', 25)
    # Se crea un objeto de la clase "Triángulo".
    w_triangulo = Triangulo('Blanco', 'Azul', 40, 80)

    # Se añaden los objetos a la lista de figuras.
    w_lista_figuras.append(w_rectangulo)
    w_lista_figuras.append(w_circulo)
    w_lista_figuras.append(w_triangulo)

    # Se recorre la lista para obtener los datos de los atributos de las figuras creadas con los objetos y el uso de sus
    # dos métodos abstractos.

    print('\n------ DATOS DE LAS FIGURAS ------')

    for r_lista_figura in w_lista_figuras:

        print('\nLos datos de la figura {} son:\n'.format(type(r_lista_figura).__name__))
        print('- Color fondo: {}'.format(r_lista_figura.a_color_fondo))
        print('- Color borde: {}\n'.format(r_lista_figura.a_color_borde))
        r_lista_figura.pro_dibujar()
        print('El área del {} es: {}'.format(type(r_lista_figura).__name__, r_lista_figura.pro_area()))

    # Se va a lanzar la sobreescrita del método "pro__str__()" que tiene la superclase con los métodos que tienen las
    # subclases del mismo nombre.

    print('\n------ SOBREESCRITURA DEL MÉTODO "PRO__STR__" DE FIGURAS ------')
    print('\n- Los datos del Rectángulo son: {}.'.format(w_rectangulo.pro__str__()))
    print('- Los datos del Círculo son: {}.'.format(w_circulo.pro__str__()))
    print('- Los datos del Triángulo son: {}.'.format(w_triangulo.pro__str__()))


# Se invoca el método app_principal() si el archivo que se está ejecutando es el main..
if __name__ == '__main__':
    app_principal()
