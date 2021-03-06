'''
Datos de la clase a crear.

  - Nombre Clase: Coche

  - Atributos:

    - Matricula.
    - Marca.
    - Modelo.
    - País procedencia.

  - Métodos:

    - Encender.
    - Apagar.
    - Acelerar.
    - Frenar.
  '''


# Creación de la clase Coche.
class Coche:

    # Se crea el inicializador de la clase siempre indicando el valor "self" para indicar que depende de la clase
    # "Coche" y luego se indican los atributos que va a tener dicha clase para así obligar a que cuando se cree un
    # objeto de ésta clase, se necesite indicar los valores que va a tener cada uno de los atributos para dicho objeto.
    def __init__(self, matricula, marca, modelo, pais_procedencia):

        # Se crea una variable de instancia para cada una de los atributos para que así se pueda usar los valores que se
        # le pasen en la llamada de la creación de un objeto de la clase "Coche".
        self.pe_matricula = matricula
        self.pe_marca = marca
        self.pe_modelo = modelo
        self.pe_pais_procedencia = pais_procedencia

        # Se crea una variable de instancia que no se indica como atributo propio de la clase "Coche" sino que sirve
        # para que su valor se pueda utilizar en toda la clase y en todos sus métodos.
        self.w_estado = False

    # Se crea los métodos de instancia que va a tener la clase "Coche.

    # Se crea el método "encender" y se indica como parámetro el valor "self" para indicar que pertenece a la clase
    # padre, en este caso, la clase "Coche".
    def encender(self):

        # Para que el coche pueda encenderse, debe de estar apagado y por ello se comprueba si el coche esta apagado.
        if not self.w_estado:
            # Se cambia el valor del estado del coche a encendido.
            self.w_estado = True

    # Se crea el método de instancia "apagar" para cambiar el estado del coche a apagado.
    def apagar(self):

        # Para que el coche pueda apagarse, debe de estar encendido y por ello se comprueba si el coche esta encendido.
        if self.w_estado:
            # Se cambia el valor del estado del coche a apagado.
            self.w_estado = False

    # Se crea el método de instancia "acelerar" para indicar por pantalla que el coche está acelerando.
    def acelerar(self):

        # Para que el coche pueda acelerar, debe de estar encendido y por ello se comprueba si el coche esta encendido.
        if self.w_estado:
            # Se muestra un mensaje por pantalla.
            print('El coche ha acelerado')

    # Se crea el método de instancia "frenar" para indicar por pantalla que el coche está frenando.
    def frenar(self):

        # Para que el coche pueda frenar, debe de estar encendido y por ello se comprueba si el coche esta encendido.
        if self.w_estado:
            # Se muestra un mensaje por pantalla.
            print('El coche ha frenado')


















