import unittest
from calificaciones.promedio import Promedios

class Test_promedios(unittest.TestCase):

    def setUp(self):
        self.calcProm = Promedios()

    def test_promediar_siete_calificaciones(self):
        resultado = self.calcProm.promedio(10,10,10,10,10,10,10)
        self.assertEqual(10.0, resultado)

    def test_promediar_dos_calificaciones_y_una_letra(self):
        resultado = self.calcProm.promedio('x',8,10)
        self.assertEqual('La calificación debe ser un numero', resultado)

    def test_promediar_tres_calificaciones_una_mayor_a_diez(self):
        resultado = self.calcProm.promedio(8,12,9)
        self.assertEqual('Calificación maxima es 10', resultado)

    def test_promediar_tres_calificaciones_una_negativa(self):
        resultado = self.calcProm.promedio(10,7,-9)
        self.assertEqual('La calificación no puede ser menor que cero', resultado)

    def test_promediar_tres_calificaciones_una_valor_flotante(self):
        resultado = self.calcProm.promedio(8,9,7.8)
        self.assertEqual('La calificación debe ser un número entero', resultado)

    def test_promediar_tres_calificaciones_una_valor_dentro_una_lista(self):
        resultado = self.calcProm.promedio(8,9,[2])
        self.assertEqual('No se pueden promediar listas', resultado)

    def test_promediar_tres_calificaciones_una_valor_boleano(self):
        resultado = self.calcProm.promedio(8,9,True)
        self.assertEqual('No se aceptan valores booleanos', resultado)


if __name__== '__main__':
    unittest.main()
