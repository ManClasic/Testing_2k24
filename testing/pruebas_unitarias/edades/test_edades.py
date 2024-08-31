import unittest
from edades.edades import Edades

class Test_edades(unittest.TestCase):

    def setUp(self):
        self.calcEdad = Edades()

    def test_edad_menor_a_cero(self):
        resultado = self.calcEdad.calc_edad(-1)
        self.assertEqual('No existes', resultado)

    def test_edad_de_tres_anios(self):
        resultado = self.calcEdad.calc_edad(3)
        self.assertEqual('Eres un niño', resultado)

    def test_edad_de_trece_anios(self):
        resultado = self.calcEdad.calc_edad(13)
        self.assertEqual('Eres un puberto', resultado)

    def test_edad_de_dieciseis_anios(self):
        resultado = self.calcEdad.calc_edad(16)
        self.assertEqual('Eres un adolecente', resultado)

    def test_edad_de_diecisiete_anios(self):
        resultado = self.calcEdad.calc_edad(17)
        self.assertEqual('Eres un adolecente', resultado)

    def test_edad_de_dieciocho_anios(self):
        resultado = self.calcEdad.calc_edad(18)
        self.assertEqual('Eres un adulto', resultado)

    def test_edad_de_veinticinco_anios(self):
        resultado = self.calcEdad.calc_edad(25)
        self.assertEqual('Eres un adulto', resultado)

    def test_edad_de_sesenta_y_uno_anios(self):
        resultado = self.calcEdad.calc_edad(61)
        self.assertEqual('Eres un adulto mayor', resultado)

    def test_edad_de_ciento_diez_anios(self):
        resultado = self.calcEdad.calc_edad(110)
        self.assertEqual('Eres un mumm-ra', resultado)

    def test_edad_de_valor_alfabetico(self):
        resultado = self.calcEdad.calc_edad('x')
        self.assertEqual('Edad solo numerica', resultado)

    def test_edad_de_valor_incompleto(self):
        resultado = self.calcEdad.calc_edad(None)
        self.assertEqual('Edad solo numerica', resultado) 

if __name__== '__main__':
    unittest.main()