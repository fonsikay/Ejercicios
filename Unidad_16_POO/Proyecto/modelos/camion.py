"""
Datos de la clase a crear.

    - Nombre Clase: Camión
    - Tipo: Subclase de Coche
    - Atributos heredados de la superclase Coche:

        + Matricula.
        + Marca.
        + Modelo.
        + País procedencia.

    - Atributos propios de la clase Camión:

        - Capacidad carga.

    - Métodos heredados de la superclase Coche:

        + pro_encender().
        + pro_apagar().
        + pro_acelerar().
        + pro_frenar().

    - Métodos propios de la clase Camión:

        - pro_cargar_mercancia().
        - pro_descargar_mercancia().
"""

# Se importa la clase principal Coche indicando con el "." que en la carpeta actual se busque el script donde se
# encuentre el archivo "coche.py" ya que si no se indica, nos da error de que no encuentra la clase Coche.
from . coche import Coche


# Se crea la clase "Camión" que es una subclase de la clase "Coche" por lo que va a heredar los atributos y métodos
# que tiene la clase "Coche" junto a los atributos y métodos propios de la clase "Camión".
class Camion(Coche):

    # Se define el contructor inicializador de la clase Camión siempre indicando el valor "self" y luego se indican
    # los atributos que va a heredar de la superclase Coche y el atributo propio de la clase "Camión".
    def __init__(self, matricula, marca, modelo, pais_procedencia, capadidad_carga):

        # Se define los atributos que va a heredar la clase Camión de la superclase o clase padre Coche.
        super().__init__(matricula, marca, modelo, pais_procedencia)

        # Se guarda en una variable de instancia, el atributo propio de la clase "Camión".
        self.a_capacidad_carga = capadidad_carga

    # Se define el método privado "pro_cargar_mercancia" de la clase "Camión".
    def pro_cargar_mercancia(self):
        print("La mercancia se está cargando...")

    # Se define el método privado "pro_descargar_mercancia" de la clase "Camión".
    def pro_descargar_mercancia(self):
        print("La mercancia se está descargando...")
