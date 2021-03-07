"""
Datos de la clase a crear.

    - Nombre Clase: Camioneta
    - Tipo: Subclase de Coche
    - Atributos heredados de la superclase Coche:

        + Matricula.
        + Marca.
        + Modelo.
        + País procedencia.

    - Atributos propios de la clase Camioneta:

        - Capacidad carga.
        - Costo servicio.

    - Métodos heredados de la superclase Coche:

        + pro_encender().
        + pro_apagar().
        + pro_acelerar().
        + pro_frenar().

    - Métodos propios de la clase Camioneta:

        - pro_cargar_material().
        - pro_descargar_material().
"""

# Se importa la clase principal Coche indicando con el "." que en la carpeta actual se busque el script donde se
# encuentre el archivo "coche.py" ya que si no se indica, nos da error de que no encuentra la clase Coche.
from . coche import Coche


# Se crea la clase Camioneta siendo subclase de la clase Coche.
class Camioneta(Coche):

    # Se crea el método inicializador de la subclase indicando los atributos heredados y propios.
    def __init__(self, matricula, marca, modelo, pais_procedencia, capacidad_carga, costo_servicio):

        # Se hace referencia al método "__init__" de la superclase "Coche" indicando sus atributos.
        super().__init__(matricula, marca, modelo, pais_procedencia)

        # Se cargan los atributos propios de la subclase "Camioneta".
        self.a_capacidad_carga = capacidad_carga
        self.a_costo_servicio = costo_servicio

    # Se crea el método privado "pro_cargar_material()" de la subclase Camioneta.
    def pro_cargar_material(self):
        print("El material se está cargando...")

    # Se crea el método privado "pro_descargar_material()" de la subclase Camioneta.
    def pro_descargar_material(self):
        print("El material se está descargando...")
