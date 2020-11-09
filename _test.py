import pytest
from clases import Juego, Palabra
import random

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



class TestJuego:
    def test_iniciar_juego(self):
        # Arrange
        j = Juego('Kent Beck')
        esperado = '****'
        # Act
        resultado = j.iniciar('CASA')
        # Assert
        assert esperado == resultado

    
    def test_cantidad_inicial_vidas(self):
        # Arrange
        j = Juego('Martin Fowler')
        esperado = 7
        # Act
        resultado = j.getVidasActuales() 
        # Assert
        assert resultado == esperado
    
    def test_quitar_vida(self):
        # Arrange
        j = Juego('Dave Thomas')
        esperado = 6
        # Act
        j.quitaVida()
        resultado = j.getVidasActuales() 
        # Assert
        assert resultado == esperado
    
    def test_arriesga_letra(self):
        # Arrange
        j = Juego('Ron Jeffries')
        esperado = 6
        # Act
        j.iniciar('CASA')
        j.arriesgarLetra('Z')
        resultado = j.getVidasActuales() 
        # Assert
        assert resultado == esperado

    def test_estado_partida(self):
        # Arrange
        j = Juego('Ron Jeffries')
        esperado = 4
        # Act
        j.iniciar('CASA')
        resultado = j.getEstado() 
        # Assert
        assert len(resultado['palabra']) == esperado
