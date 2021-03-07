"""
Datos de la clase a crear.

    - Nombre Clase: Perro
    - Tipo: Subclase de Animal
    - Atributos heredados de la superclase Animal:

        - Nombre.
        - Edad.
        - Nombre científico.

    - Atributos propios de la clase Perro:

        - Raza.

    - Métodos heredados de la superclase Animal:

        + pro_comer().
        + pro_moverse().
        + Abstracto pro_hablar().

    - Métodos propios de la clase Perro:

        + pro_jugar().
        + Abstracto pro_hablar().
"""

# Se importa la superclase "Animal".
from .animal import Animal


# Se crea la subclase Perro de la superclase Animal.
class Perro(Animal):

    # Definición del constructor con los atributos heredados y propios
    def __init__(self, nombre, edad, nombre_cientifico, raza):

        # Se llama al método inicializador de la superclase Animal.
        super(Perro, self).__init__(nombre, edad, nombre_cientifico)

        # Se crean las variables de instancia de los atributos propios.
        self.a_raza = raza

    # Se define el método propio "pro_jugar()".
    def pro_jugar(self):
        print('El perro esta jugando...')

    # Se define el funcionamiento del método abstracto heredado "pro_hablar()" de la superclase "Animal".
    def pro_hablar(self):
        print('Guau!')
