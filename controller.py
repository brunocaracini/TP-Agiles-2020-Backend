from clases import Juego
import pymongo


class Controller:

    def __init__(self):
        pass

    @classmethod
    def iniciar_partida(self, nombre):
        j = Juego(nombre)
        j.iniciar()
        return j

    @classmethod
    def enviar_letra(self, letra, j):
        j.arriesgarLetra(letra)
        return j

    @classmethod
    def enviar_palabra(self, palabra, j):
        j.arriesgarPalabra(palabra)
        return j

