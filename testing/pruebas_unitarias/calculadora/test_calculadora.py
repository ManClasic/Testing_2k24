import unittest
from pruebas_doctest.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def tearDown(self):
        pass


    def test_sumar_dos_mas_dos(self):
        resultado = self.calc.sumar(2,2)
        self.assertEqual(4, resultado)

        def sumar_tres_mas_dos(self):
            calc = Calculadora()
            resultado = calc.sumar(3,2)
            self.assertEqual(5, resultado)


if __name__== '__main__':
    unittest.main()