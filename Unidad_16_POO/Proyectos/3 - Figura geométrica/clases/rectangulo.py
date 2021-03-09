# Creación de la subclase "Rectangulo" con dos métodos.

"""
Datos de la clase a crear.

    - Nombre Clase: Rectangulo
    - Tipo: Subclase de Figura
    - Atributos heredados de la superclase Figura:

        - Color fondo.
        - Color borde.

    - Atributos propios de la clase Rectangulo:

        - Ancho.
        - Alto.

    - Métodos abstractos heredados de la superclase Figura:

        + pro_dibujar().
        + pro_area().
        + pro__str__().
"""

# Se importa la superclase Figura del archivo "figura.py".
from .figura import Figura


# Se crea la subclase "Rectangulo" de la superclase "Figura".
class Rectangulo(Figura):

    # Definición del constructor con los atributos heredados y propios.
    def __init__(self, color_fondo, color_borde, ancho, alto):

        # Se llama al método inicializador de la superclase Figura.
        super(Rectangulo, self).__init__(color_fondo, color_borde)

        # Se crean las variables de instancia de los atributos propios.
        self.a_ancho = ancho
        self.a_alto = alto

    # Se define el funcionamiento del método abstracto heredado "pro_dibujar()" de la superclase "Figura".
    def pro_dibujar(self):
        print('Se está dibujando el rectángulo de {} de ancho por {} de alto.'.format(self.a_ancho, self.a_alto))

    # Se define el funcionamiento del método abstracto heredado "pro_area()" de la superclase "Figura".
    def pro_area(self):

        # Se calcula el area de un rectángulo (ancho por alto) y se retorna.
        w_area = self.a_ancho * self.a_alto
        return w_area

    # Se crea el método "pro__str__()" para que se pueda imprimir por pantalla los datos de los dos atributos que tiene
    # la clase figura y le añadimos los atributos propios de la clase Rectangulo.
    # Se obtiene lo que tiene el método "pro__str__()" de la clase padre con el comando "super()".
    def pro__str__(self):
        return '{} - Ancho: {}. - Alto: {}'.format(super().pro__str__(), self.a_ancho, self.a_alto)
