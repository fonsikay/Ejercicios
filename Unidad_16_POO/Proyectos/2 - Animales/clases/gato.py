"""
Datos de la clase a crear.

    - Nombre Clase: Gato
    - Tipo: Subclase de Animal
    - Atributos heredados de la superclase Animal:

        - Nombre.
        - Edad.
        - Nombre científico.

    - Atributos propios de la clase Gato:

        - Domestico.

    - Métodos heredados de la superclase Animal:

        + pro_comer().
        + pro_moverse().
        + Abstracto pro_hablar().

    - Métodos propios de la clase Gato:

        + pro_ronronear().
        + Abstracto pro_hablar().
"""

# Se importa la superclase "Animal".
from .animal import Animal


# Se crea la subclase Gato de la superclase Animal.
class Gato(Animal):

    # Definición del constructor con los atributos heredados y propios
    def __init__(self, nombre, edad, nombre_cientifico, domestico):

        # Se llama al método inicializador de la superclase Animal.
        super(Gato, self).__init__(nombre, edad, nombre_cientifico)

        # Se crean las variables de instancia de los atributos propios.
        self.a_domestico = domestico

    # Se define el método propio "pro_ronronear()".
    def pro_ronronear(self):
        print('El gato está ronroneando...')

    # Se define el funcionamiento del método abstracto heredado "pro_hablar()" de la superclase "Animal".
    def pro_hablar(self):
        print('Miau!')
