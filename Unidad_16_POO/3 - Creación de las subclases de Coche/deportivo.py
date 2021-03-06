'''
Datos de la clase a crear.

    - Nombre Clase: Deportivo

    - Atributos públicos heredados de la superclase Coche:

        + Matricula.
        + Marca.
        + Modelo.
        + País procedencia.

    - Atributos privados de la clase Deportivo:

        - Marca Rines.
        - Tipo.

    - Métodos públicos heredados de la superclase Coche:

        + Encender().
        + Apagar().
        + Acelerar().
        + Frenar().

    - Métodos privados de la clase Deportivo:

        - pro_abrir_puertas().
'''

# Se importa la clase principal Coche.
from coche import Coche


# Se crea la clase Deportivo siendo subclase de la clase Coche.
class Deportivo(Coche):

    # Se crea el método inicializador de la subclase indicando los atributos heredados y propios.
    def __init__(self, matricula, marca, modelo, pais_procedencia, marca_rines, tipo):

        # Se hace referencia al método "__init__" de la superclase "Coche" indicando sus atributos.
        super().__init__(matricula, marca, modelo, pais_procedencia)

        # Se cargan los atributos propios de la subclase "Deportivo".
        self.a_marca_rines = marca_rines
        self.a_tipo = tipo

    # Se crea el método privado "pro_abrir_puertas()" de la subclase Deportivo.
    def pro_abrir_puertas(self):
        pass
