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

    - Métodos abstractos heredados de la superclase Figura:

        + pro_dibujar().
        + pro_area().
        + pro__str__().
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
        print('Se está dibujando el triángulo de {} de base y {} de altura.'.format(self.a_base, self.a_altura))

    # Se define el funcionamiento del método abstracto heredado "pro_area()" de la superclase "Figura".
    def pro_area(self):

        # Se calcula el area del triángulo (base por altura entre dos) y se retorna.
        w_area = (self.a_base * self.a_altura) / 2
        return w_area

    # Se crea el método "pro__str__()" para que se pueda imprimir por pantalla los datos de los dos atributos que tiene
    # la clase figura y le añadimos los atributos propios de la clase Triángulo.
    # Se obtiene lo que tiene el método "pro__str__()" de la clase padre con el comando "super()".
    def pro__str__(self):
        return '{} - Base: {}. - Altura: {}'.format(super(Triangulo, self).pro__str__(), self.a_base, self.a_altura)