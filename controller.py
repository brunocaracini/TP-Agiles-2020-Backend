from clases import Juego
import pymongo
from dbcontroller import DBController
import random

class Controller:

    def __init__(self):
        pass

    @classmethod
    def iniciar_partida(self, nombre):
        j = Juego(nombre)
        j.iniciar(self.obtenerPalabra())
        return j

    @classmethod
    def enviar_letra(self, letra, j):
        j.arriesgarLetra(letra)
        return j

    @classmethod
    def enviar_palabra(self, palabra, j):
        j.arriesgarPalabra(palabra)
        return j

    @classmethod
    def obtenerPalabra(self):
        DBController.openConn()
        palabras = DBController.getAll()
        return random.choice(palabras)
