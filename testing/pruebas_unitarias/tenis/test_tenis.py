import unittest
from tenis import tenisMatch

class Test_tenis(unittest.TestCase):

    def setUp(self):
        self.setTenis = tenisMatch()

    def test_jugadores_en_0s(self):
        resultado = self.setTenis.obtener_score()
        self.assertEqual('Jugador 1: 0 - Jugador 2: 0', resultado)

    def test_jugador1_anota_primero_que_el_jugador2(self):
        self.setTenis.anotar_punto(1)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('Jugador 1: 15 - Jugador 2: 0', resultado)

    def test_jugador2_anota_primero_que_el_jugador1(self):
        self.setTenis.anotar_punto(2)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('Jugador 1: 0 - Jugador 2: 15', resultado)

    def test_jugador1_gana_jugador2_sin_puntos(self):
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(1)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('El juego ha terminado.', resultado)

    def test_jugador2_gana_jugado12_sin_puntos(self):
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(2)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('El juego ha terminado.', resultado)

    def test_empate_ambos_jugadpres_50_puntos_puntos_intercalados(self):
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('Deuce', resultado)

    def test_jugador1_ventaja_despues_de_deuce(self):
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('Ventaja Jugador 1', resultado)

    def test_jugador2_ventaja_despues_de_deuce(self):
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(2)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('Ventaja Jugador 2', resultado)

    def test_jugador1_gana_despues_de_ventaja_despues_de_deuce(self):
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(1)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('El juego ha terminado.', resultado)

    def test_jugador2_gana_despues_de_ventaja_despues_de_deuce(self):
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(1)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(2)
        self.setTenis.anotar_punto(2)
        resultado = self.setTenis.obtener_score()
        self.assertEqual('El juego ha terminado.', resultado)


if __name__== '__main__':
    unittest.main()