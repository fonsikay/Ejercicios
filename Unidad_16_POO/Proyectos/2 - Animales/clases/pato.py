"""
Datos de la clase a crear.

    - Nombre Clase: Pato
    - Tipo: Subclase de Animal
    - Atributos heredados de la superclase Animal:

        - Nombre.
        - Edad.
        - Nombre científico.

    - Atributos propios de la clase Pato:

        - Color.

    - Métodos heredados de la superclase Animal:

        + pro_comer().
        + pro_moverse().
        + Abstracto pro_hablar().

    - Métodos propios de la clase Pato:

        + pro_volar().
        + Abstracto pro_hablar().
"""

# Se importa la superclase "Animal".
from .animal import Animal


# Se crea la subclase Pato de la superclase Animal.
class Pato(Animal):

    # Definición del constructor con los atributos heredados y propios
    def __init__(self, nombre, edad, nombre_cientifico, color):

        # Se llama al método inicializador de la superclase Animal.
        super(Pato, self).__init__(nombre, edad, nombre_cientifico)

        # Se crean las variables de instancia de los atributos propios.
        self.a_color = color

    # Se define el método propio "pro_volar()".
    def pro_volar(self):
        print('El pato está volando...')

    # Se define el funcionamiento del método abstracto heredado "pro_hablar()" de la superclase "Animal".
    def pro_hablar(self):
        print('Cuá Cuá!')
