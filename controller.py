from clases import Juego
from dbcontroller import DBController

class Controller:

    def __init__(self):
        pass

    @classmethod
    def iniciar_partida(self, nombre):
        j = Juego(nombre)
        j.iniciar(DBController.getRandomWord())
        return j

    @classmethod
    def enviar_letra(self, letra, j):
        j.arriesgarLetra(letra)
        return j

    @classmethod
    def enviar_palabra(self, palabra, j):
        j.arriesgarPalabra(palabra)
        return j
