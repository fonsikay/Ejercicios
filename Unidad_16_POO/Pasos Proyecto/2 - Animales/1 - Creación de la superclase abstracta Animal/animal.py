# Creación de la superclase abstracta "Animal" con varios métodos y uno de ellos que sea abstracto.

"""
Datos de la clase a crear.

    - Nombre Clase: Animal
    - Tipo: Superclase Abstracta

    - Atributos propios de la clase:

        - Nombre.
        - Edad.
        - Nombre científico.

    - Métodos propios de la clase:

        + pro_comer().
        + pro_moverse().
        + Abstracto pro_hablar().
"""

# Si una clase es abstracta, no es posible crear un objeto de dicha clase pero si se pueden utilizar sus métodos y
# atributos en otras subclases relacionadas.

# Se importa la librería "abc" para importar la clase "ABC" que hace que una clase pueda ser abstracta y la clase
# "abstractmethod" que hace que un método pueda ser abstracto.
from abc import ABC, abstractmethod


# Se crea la clase abstracta "Animal".
class Animal(ABC):

    # Definición del constructor con los atributos.
    def __init__(self, nombre, edad, nombre_cientifico):

        # Se crean las variables de instancia de los atributos de la clase Animal.
        self.a_nombre = nombre
        self.a_edad = edad
        self.a_nombre_cientifico = nombre_cientifico

    # Se definen los métodos de instancia.
    def pro_comer(self):
        print('El animal está comiendo...')

    def pro_moverse(self):
        print('El animal se está moviendo...')

    # Se define el método de instancia abstracto utilizando "@abstractmethod" y en su código se pone "pass" porque su
    # funcionamiento se va a declarar en cada una de las subclases que la vayan a utilizar.
    @abstractmethod
    def pro_hablar(self):
        pass
