"""
Datos de la clase a crear.

    - Nombre Clase: Deportivo
    - Tipo: Subclase de Coche
    - Atributos heredados de la superclase Coche:

        + Matricula.
        + Marca.
        + Modelo.
        + País procedencia.

    - Atributos propios de la clase Deportivo:

        - Marca Llantas.
        - Tipo deportivo.

    - Métodos heredados de la superclase Coche:

        + Encender().
        + Apagar().
        + Acelerar().
        + Frenar().

    - Métodos propios de la clase Deportivo:

        - pro_abrir_puertas().
        - pro_cerrar_puertas().
"""

# Se importa la clase principal Coche indicando con el "." que en la carpeta actual se busque el script donde se
# encuentre el archivo "coche.py" ya que si no se indica, nos da error de que no encuentra la clase Coche.
from . coche import Coche


# Se crea la clase Deportivo siendo subclase de la clase Coche.
class Deportivo(Coche):

    # Se crea el método inicializador de la subclase indicando los atributos heredados y propios.
    def __init__(self, matricula, marca, modelo, pais_procedencia, marca_llantas, tipo_deportivo):

        # Se hace referencia al método "__init__" de la superclase "Coche" indicando sus atributos.
        super().__init__(matricula, marca, modelo, pais_procedencia)

        # Se cargan los atributos propios de la subclase "Deportivo".
        self.a_marca_llantas = marca_llantas
        self.a_tipo_deportivo = tipo_deportivo

    # Se crea el método privado "pro_abrir_puertas()" de la subclase Deportivo.
    def pro_abrir_puertas(self):
        print("El deportivo esta abriendo las puertas...")

    # Se crea el método privado "pro_cerrar_puertas()" de la subclase Deportivo.
    def pro_cerrar_puertas(self):
        print("El deportivo esta cerrando las puertas...")
