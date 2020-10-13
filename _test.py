import pytest
from clases import Juego, Palabra

class TestPalabra:
    def test_valida_letra_a_en_palabra_casa(self):
        # Arrange
        p = Palabra('casa')
        esperado = True
        # Act
        resultado = p.validaLetra('A') 
        # Assert
        assert esperado == resultado

    def test_valida_letra_z_en_palabra_casa(self):
        # Arrange
        p = Palabra('casa')
        esperado = False
        # Act
        resultado = p.validaLetra('Z') 
        # Assert
        assert esperado == resultado

    def test_valida_estado_palabra_casa(self):
        # Arrange
        p = Palabra('casa')
        esperado = '****'
        # Act
        resultado = p.getEstado() 
        # Assert
        assert esperado == resultado

    def test_valida_estado_palabra_casa_con_letra_A(self):
        # Arrange
        p = Palabra('casa')
        esperado = '*A*A'
        # Act
        p.validaLetra('A')
        resultado = p.getEstado() 
        # Assert
        assert esperado == resultado

    def test_valida_agregar_letra_a_lista(self):
        # Arrange
        p = Palabra('casa')
        esperado = ['A', 'S']
        # Act
        p.validaLetra('A')
        p.validaLetra('S')
        resultado = p.getLetrasArriesgadas() 
        # Assert
        assert esperado == resultado

    def test_valida_agregar_letra_ya_agregada_a_lista(self):
        # Arrange
        p = Palabra('casa')
        esperado = ['A', 'S']
        # Act
        p.validaLetra('A')
        p.validaLetra('S')
        p.validaLetra('S')
        resultado = p.getLetrasArriesgadas() 
        # Assert
        assert esperado == resultado 

    def test_valida_arriesgar_palabra_correcta(self):
        # Arrange
        p = Palabra('casa')
        esperado = True
        # Act
        resultado = p.validaPalabra('casa')
        # Assert
        assert esperado == resultado 

    def test_valida_arriesgar_palabra_incorrecta(self):
        # Arrange
        p = Palabra('casa')
        esperado = False
        # Act
        resultado = p.validaPalabra('helicoptero')
        # Assert
        assert esperado == resultado  



class TestPartida:
    def test_iniciar_partida(self):
        # Arrange
        j = Juego()
        esperado = '*******'
        # Act
        resultado = j.iniciar() 
        # Assert
        assert esperado == resultado

    def test_obtener_palabra_valida(self):
        # Arrange
        j = Juego()
        esperado = ['PRUEBA1', 'PRUEBA2', 'PRUEBA3']
        # Act
        resultado = j.obtenerPalabra() 
        # Assert
        assert resultado in esperado