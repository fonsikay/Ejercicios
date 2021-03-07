# Creación de la superclase abstracta "Figura" con dos métodos abstractos.

"""
Datos de la clase a crear.

    - Nombre Clase: Figura
    - Tipo: Superclase Abstracta

    - Atributos propios de la clase:

        - Color fondo.
        - Color borde.

    - Métodos propios de la clase:

        + Abstracto pro_dibujar().
        + Abstracto pro_area().
"""

# Se importa la libreria "abc" para poder indicar la clase y los métodos como abstractos.
from abc import ABC, abstractmethod


# Se crea la clase abstracta "Figura".
class Figura(ABC):

    # Definición del constructor con los atributos.
    def __init__(self, color_fondo, color_borde):

        # Se crean las variables de instancia de los atributos de la clase Figura.
        self.a_color_fondo = color_fondo
        self.a_color_borde = color_borde

    # Se crea el método abstracto "pro_dibujar()" que se indicará su funcionalidad en las subclases.
    @abstractmethod
    def pro_dibujar(self):
        pass

    # Se crea el método abstracto "pro_area()" que se indicará su funcionalidad en las subclases.
    @abstractmethod
    def pro_area(self):
        pass
