# Creación de la subclase "Triangulo" con dos métodos.

"""
Datos de la clase a crear.

    - Nombre Clase: Circulo
    - Tipo: Subclase de Figura
    - Atributos heredados de la superclase Figura:

        - Color fondo.
        - Color borde.

    - Atributos propios de la clase Triangulo:

        - Base.
        - Altura.

    - Métodos heredados de la superclase Figura:

        + pro_dibujar().
        + pro_area().
"""

# Se importa la superclase Figura del archivo "figura.py".
from .figura import Figura


# Se crea la subclase "Triangulo" de la superclase "Figura".
class Triangulo(Figura):

    # Definición del constructor con los atributos heredados y propios.
    def __init__(self, color_fondo, color_borde, base, altura):

        # Se llama al método inicializador de la superclase Figura.
        super(Triangulo, self).__init__(color_fondo, color_borde)

        # Se crean las variables de instancia de los atributos propios.
        self.a_base = base
        self.a_altura = altura

    # Se define el funcionamiento del método abstracto heredado "pro_dibujar()" de la superclase "Figura".
    def pro_dibujar(self):
        pass

    # Se define el funcionamiento del método abstracto heredado "pro_area()" de la superclase "Figura".
    def pro_area(self):
        pass
