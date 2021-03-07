"""
Datos de la clase a crear.

    - Nombre Clase: Formula1
    - Tipo: Subclase de Coche
    - Atributos heredados de la superclase Coche:

        + Matricula.
        + Marca.
        + Modelo.
        + País procedencia.

    - Atributos propios de la clase Formula1:

        - Peso

    - Métodos heredados de la superclase Coche:

        + pro_encender().
        + pro_apagar().
        + pro_acelerar().
        + pro_frenar().

    - Métodos propios de la clase Formula1:

        - pro_competir().
"""

# Se importa la clase principal Coche indicando con el "." que en la carpeta actual se busque el script donde se
# encuentre el archivo "coche.py" ya que si no se indica, nos da error de que no encuentra la clase Coche.
from .coche import Coche


# Se crea la clase Camioneta siendo subclase de la clase Coche.
class Formula1(Coche):

    # Se crea el método inicializador de la subclase indicando los atributos heredados y propios.
    def __init__(self, matricula, marca, modelo, pais_procedencia, peso):

        # Se hace referencia al método "__init__" de la superclase "Coche" indicando sus atributos.
        super().__init__(matricula, marca, modelo, pais_procedencia)

        # Se cargan los atributos propios de la subclase "Formula 1".
        self.a_peso = peso

    # Se crea el método privado "pro_competir()" de la subclase Formula 1.
    def pro_competir(self):
        print("El Formula 1 está compitiendo...")
