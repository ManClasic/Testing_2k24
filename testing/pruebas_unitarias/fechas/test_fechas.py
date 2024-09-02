import unittest
from fechas.fechas import Fechas

class Test_fechas(unittest.TestCase):

    def setUp(self):
        self.calc_fecha = Fechas()

    def test_fecha_de_nacimiento_14_06_1998(self):
        resultado = self.calc_fecha.conv_fecha('14/06/1998')
        self.assertEqual('Catorce de Junio del mil nuevecientos noventa y ocho', resultado)


if __name__== '__main__':
    unittest.main()