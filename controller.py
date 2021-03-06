from clases import Juego
from data import Data

class Controller:

    def __init__(self):
        pass

    @classmethod
    def iniciar_partida(self, nombre, dificultad):
        j = Juego(nombre)
        j.iniciar(None, dificultad)
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
    def get_ranking(self):
        return Data.getRanking()

