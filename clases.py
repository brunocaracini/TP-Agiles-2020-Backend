import enum
from data import Data

class Palabra():

	def __init__(self, p): 
		self.palabra = p.upper()
		self.letrasArriesgadas = []
		self.puntajeDificultad = self.getPuntajeDificultad()
		self.dificultad = self.getDificultad()

	def getPalabra(self):
		return self.palabra

	def getLetrasArriesgadas(self):
		return self.letrasArriesgadas

	def validaLetra(self, letra):
		if letra.upper() not in self.letrasArriesgadas:
			self.letrasArriesgadas.append(letra.upper()) 
		return letra.upper() in self.palabra

	def validaPalabra(self, palabra):		 
		return palabra.upper() == self.palabra

	def getEstado(self, estado_partida='CURSO'):
		if estado_partida != 'CURSO':
			estado = self.palabra
		else:
			estado = ''
			for letra in self.palabra:
				if letra in self.letrasArriesgadas:
					estado += letra
				else:
					estado += '*'
		return estado

	def getPuntajeDificultad(self):
		letters = 'EAOSRNIDLCTUMPBGVYQHFZJÑXKW'
		vowels = set('AEIOU')
		word = self.getPalabra()
		unique = set(word)
		positions = sum(letters.index(c) for c in word)
		return len(word) * len(unique) * (7 - len(unique & vowels)) * positions
	
	def getDificultad(self):
		if self.puntajeDificultad <= 2000:
			return 'FACIL'
		elif self.puntajeDificultad > 2000 and self.puntajeDificultad <15000:
			return 'MEDIA'
		else:
			return 'DIFICIL'
	
class Juego():
 
	def __init__(self, nombreJugador):
		self.nombreJugador = nombreJugador
		self.estadoPartida = 'CURSO'
		self.puntaje = 0 
		self.palabraActual = None
		self.cantInicialVidas = 7
		self.cantActualVidas = self.cantInicialVidas
		self.dificultad = None

	def iniciar(self, palabra, dificultad='MEDIA'):
		if palabra == None:
			self.palabraActual = Palabra(Data.getRandomWord(dificultad))
		else:
			self.palabraActual = Palabra(palabra)
		self.dificultad = dificultad
		return self.palabraActual.getEstado()
	
	def getVidasActuales(self):
		return self.cantActualVidas
	
	def quitaVida(self):
		if self.cantActualVidas == 1:
			self.estadoPartida = 'PERDIDA'
		self.cantActualVidas -= 1
	
	def arriesgarLetra(self, letra):
		res = self.palabraActual.validaLetra(letra)
		if not res:
			self.quitaVida()

		if self.palabraActual.getPalabra() == self.palabraActual.getEstado():
			self.estadoPartida = 'GANADA'
			self.calcularPuntaje()
			Data.actualizaRanking(self.puntaje, self.nombreJugador)

		return res

	def arriesgarPalabra(self, palabra):
		if self.palabraActual.validaPalabra(palabra):
			self.estadoPartida = 'GANADA'
			self.calcularPuntaje(500)
			Data.actualizaRanking(self.puntaje, self.nombreJugador)
		else:
			self.quitaVida()

	def calcularPuntaje(self,bonus=0):
		if self.cantActualVidas == self.cantInicialVidas:
			cantidad_fallos = 0.9
		else:
			cantidad_fallos = self.cantInicialVidas - self.cantActualVidas
		if self.dificultad == 'FACIL':
			self.puntaje = int(round((len(self.palabraActual.getPalabra())/cantidad_fallos)*100*self.cantActualVidas + bonus,0))
		elif self.dificultad == 'MEDIA':
			self.puntaje = int(round((len(self.palabraActual.getPalabra())/cantidad_fallos)*125*self.cantActualVidas + bonus,0))
		else:
			self.puntaje = int(round((len(self.palabraActual.getPalabra())/cantidad_fallos)*150*self.cantActualVidas + bonus,0))

	def getEstado(self):
		return {
			'palabra': self.palabraActual.getEstado(self.estadoPartida),
			'estadoPartida': self.estadoPartida,
			'nombreJugador': self.nombreJugador,
			'cantActualVidas': self.cantActualVidas,
			'letrasArriesgadas': self.palabraActual.getLetrasArriesgadas(),
			'dificultad':self.dificultad,
			'puntaje': self.puntaje
		}

