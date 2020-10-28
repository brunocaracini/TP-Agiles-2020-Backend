import random
import enum

class Palabra():

	def __init__(self, p): 
		self.palabra = p.upper()
		self.letrasArriesgadas = []

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

	def getEstado(self):
		estado = ''
		for letra in self.palabra:
			if letra in self.letrasArriesgadas:
				estado += letra
			else:
				estado += '*'
		return estado

"""
   PERDIDA = 1
   GANADA = 2
   CURSO = 3
"""

class Juego():
 
	def __init__(self, nombreJugador):
		self.nombreJugador = nombreJugador
		self.estadoPartida = 3
		self.puntaje = 0 
		self.palabraActual = None
		self.cantInicialVidas = 7
		self.cantActualVidas = self.cantInicialVidas

	def iniciar(self):
		self.palabraActual = Palabra(self.obtenerPalabra())
		return self.palabraActual.getEstado()

	def obtenerPalabra(self):
		palabras = ['PRUEBA1', 'PRUEBA2', 'PRUEBA3']
		return random.choice(palabras)
	
	def getVidasActuales(self):
		return self.cantActualVidas
	
	def quitaVida(self):
		if self.cantActualVidas == 1:
			self.estadoPartida = 1
		self.cantActualVidas -= 1
	
	def arriesgarLetra(self, letra):
		res = self.palabraActual.validaLetra(letra)
		if not res:
			self.quitaVida()

		if self.palabraActual.getPalabra() == self.palabraActual.getEstado():
			self.estadoPartida = 2

		return res

	def getEstado(self):
		return {
			'palabra': self.palabraActual.getEstado(),
			'estadoPartida': self.estadoPartida,
			'nombreJugador': self.nombreJugador,
			'cantActualVidas': self.cantActualVidas
		}


	

	
	


