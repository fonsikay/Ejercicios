# Creación de la subclase "Circulo" con dos métodos.

"""
Datos de la clase a crear.

    - Nombre Clase: Circulo
    - Tipo: Subclase de Figura
    - Atributos heredados de la superclase Figura:

        - Color fondo.
        - Color borde.

    - Atributos propios de la clase Circulo:

        - Radio.

    - Métodos abstractos heredados de la superclase Figura:

        + pro_dibujar().
        + pro_area().
        + pro__str__().
"""

# Se importa la superclase Figura del archivo "figura.py".
from .figura import Figura
from math import pi


# Se crea la subclase "Circulo" de la superclase "Figura".
class Circulo(Figura):

    # Definición del constructor con los atributos heredados y propios.
    def __init__(self, color_fondo, color_borde, radio):

        # Se llama al método inicializador de la superclase Figura.
        super(Circulo, self).__init__(color_fondo, color_borde)

        # Se crean las variables de instancia de los atributos propios.
        self.a_radio = radio

    # Se define el funcionamiento del método abstracto heredado "pro_dibujar()" de la superclase "Figura".
    def pro_dibujar(self):
        print('Se está dibujando el círculo de {} de radio.'.format(self.a_radio))

    # Se define el funcionamiento del método abstracto heredado "pro_area()" de la superclase "Figura".
    def pro_area(self):

        # Se calcula el area de un circulo (pi por radio al cuadrado) y se retorna.
        w_area = pi * (self.a_radio ** 2)
        return w_area

    # Se crea el método "pro__str__()" para que se pueda imprimir por pantalla los datos de los dos atributos que tiene
    # la clase figura y le añadimos los atributos propios de la clase Círculo.
    # Se obtiene lo que tiene el método "pro__str__()" de la clase padre con el comando "super()".
    def pro__str__(self):
        return '{} - Radio: {}'.format(super(Circulo, self).pro__str__(), self.a_radio)
