import unittest
from calculadora.calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def tearDown(self):
        pass


    def test_sumar_dos_mas_dos(self):
        resultado = self.calc.sumar(2,2)
        self.assertEqual(4, resultado)

    '''La funcion a probar tiene que llamarse igual que la clase, si no no se ejecuta la prueba
    test_sumar_dos_mas_dos   a comparacion de sumar_tres_mas_dos. esta ultima se ejecutaria por el nombre desigual'''

    def test_sumar_tres_mas_dos(self):
        resultado = self.calc.sumar(3,2)
        self.assertEqual(5, resultado)

    def test_sumar_menos_dos_mas_tres(self):
        resultado = self.calc.sumar(-2,3)
        self.assertEqual('solo numeros positivos', resultado)

    def test_sumar_una_letra_mas_tres(self):
        resultado = self.calc.sumar('x',3)
        self.assertEqual('solo se pueden sumar numeros', resultado)

    def test_sumar_incompleto_mas_dos(self):
        resultado = self.calc.sumar(2,None)
        self.assertEqual('solo se pueden sumar numeros', resultado)

    def test_sumar_una_listao_mas_dos(self):
        resultado = self.calc.sumar([2],2)
        self.assertEqual('solo se pueden sumar numeros', resultado)

    def test_sumar_tres_punto_cinco_mas_tres(self):
        resultado = self.calc.sumar(3.5,3)
        self.assertEqual('solo se pueden sumar numeros enteros', resultado)

    #termina modulo de sumas

    def test_restar_tres_menos_dos(self):
        resultado = self.calc.restar(3,2)
        self.assertEqual(1, resultado)

    def test_restar_dos_menos_tres(self):
        resultado = self.calc.restar(2,3)
        self.assertEqual(-1, resultado)

    def test_restar_tres_punto_cinco_menos_tres(self):
        resultado = self.calc.restar(3.5,3)
        self.assertEqual('solo se pueden restar numeros enteros', resultado)

    def test_restar_incompleto_menos_dos(self):
        resultado = self.calc.restar(2,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_restar_incompleto_menos_incompleto(self):
        resultado = self.calc.restar(None,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_restar_una_listao_menos_dos(self):
        resultado = self.calc.restar([2],2)
        self.assertEqual('no se pueden restar listas', resultado)

    def test_restar_menos_dos_menos_tres(self):
        resultado = self.calc.restar(-2,3)
        self.assertEqual('solo numeros positivos', resultado)

    def test_restar_una_letra_menos_tres(self):
        resultado = self.calc.restar('x',3)
        self.assertEqual('solo se pueden restar numeros', resultado)

    #termina modulo de restas

    def test_multiplica_nueve_por_nueve(self):
        resultado = self.calc.multiplicar(9,9)
        self.assertEqual(81, resultado)

    def test_multiplica_dos_por_cinco(self):
        resultado = self.calc.multiplicar(2,5)
        self.assertEqual(10, resultado)

    def test_multiplica_nueve_punto_cinco_por_tres(self):
        resultado = self.calc.multiplicar(9.5,3)
        self.assertEqual('solo se pueden multiplicar numeros enteros', resultado)

    def test_multiplica_dos_por_valor_vacio(self):
        resultado = self.calc.multiplicar(2,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_multiplica_valor_vacio_por_valor_vacio(self):
        resultado = self.calc.multiplicar(None,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_multiplica_dos_por_una_lista_de_elementos(self):
        resultado = self.calc.multiplicar(2,[2])
        self.assertEqual('no se pueden multiplicar listas', resultado)

    def test_multiplica_menos_dos_por_tres(self):
        resultado = self.calc.multiplicar(-2,3)
        self.assertEqual('solo numeros positivos', resultado)

    def test_multiplica_una_letra_por_tres(self):
        resultado = self.calc.multiplicar('x',3)
        self.assertEqual('solo se pueden multiplicar numeros', resultado)

    #termina modulo de multiplicaciones

    def test_divide_cincuenta_entre_dos(self):
        resultado = self.calc.dividir(50,2)
        self.assertEqual(25, resultado)

    def test_divide_veinte_entre_dos(self):
        resultado = self.calc.dividir(20,2)
        self.assertEqual(10, resultado)

    def test_divide_nueve_punto_cinco_entre_tres(self):
        resultado = self.calc.dividir(9.5,3)
        self.assertEqual('solo se pueden dividir numeros enteros', resultado)

    def test_divide_dos_entre_valor_vacio(self):
        resultado = self.calc.dividir(2,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_divide_valor_vacio_entre_valor_vacio(self):
        resultado = self.calc.dividir(None,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_divide_dos_entre_una_lista_de_elementos(self):
        resultado = self.calc.dividir(2,[2])
        self.assertEqual('no se pueden dividir listas', resultado)

    def test_divide_menos_dos_entre_tres(self):
        resultado = self.calc.dividir(-2,3)
        self.assertEqual('solo numeros positivos', resultado)

    def test_divide_una_letra_entre_tres(self):
        resultado = self.calc.dividir('x',3)
        self.assertEqual('solo se pueden dividir numeros', resultado)

    def test_divide_cinco_entre_cero(self):
        resultado = self.calc.dividir(5,0)
        self.assertEqual('como vas a dividir entre cero papito...', resultado)

    #termina modulo de divisiones

    def test_eleva_tres_a_la_tres(self):
        resultado = self.calc.elevar(3,3)
        self.assertEqual(27, resultado)

    def test_eleva_dos_a_la_dos(self):
        resultado = self.calc.elevar(2,2)
        self.assertEqual(4, resultado)

    def test_eleva_nueve_punto_cinco_a_la_tres(self):
        resultado = self.calc.elevar(9.5,3)
        self.assertEqual('solo se pueden elevar numeros enteros', resultado)

    def test_eleva_cuatro_a_la_valor_vacio(self):
        resultado = self.calc.elevar(4,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_eleva_valor_vacio_a_la_valor_vacio(self):
        resultado = self.calc.elevar(None,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_eleva_dos_a_la_una_lista_de_elemntos(self):
        resultado = self.calc.elevar(2,[2])
        self.assertEqual('no se pueden elevar listas', resultado)

    def test_eleva_menos_dos_a_la_tres(self):
        resultado = self.calc.elevar(-2,3)
        self.assertEqual('solo numeros positivos', resultado)

    def test_eleva_una_letra_a_la_tres(self):
        resultado = self.calc.elevar('x',3)
        self.assertEqual('solo se pueden elevar numeros', resultado)

    #termina modulo de potencias 

    def test_raiz_de_ochenta_uno_entre_dos(self):
        resultado = self.calc.raiz(81,2)
        self.assertEqual(9.0, resultado)

    def test_raiz_de_veinte_cinco_entre_dos(self):
        resultado = self.calc.raiz(25,2)
        self.assertEqual(5.0, resultado)

    def test_raiz_de_nueve_punto_cinco_entre_tres(self):
        resultado = self.calc.raiz(9.5,3)
        self.assertEqual('solo se puede sacar raiz de numeros enteros', resultado)

    def test_raiz_de_valor_vacio_entre_cuatro(self):
        resultado = self.calc.raiz(None,4)
        self.assertEqual('operacion incompleta', resultado)

    def test_raiz_de_valor_vacio_entre_valor_vacio(self):
        resultado = self.calc.raiz(None,None)
        self.assertEqual('operacion incompleta', resultado)

    def test_raiz_de_dos_entre_una_lista_de_elementos(self):
        resultado = self.calc.raiz(2,[2])
        self.assertEqual('no se puede sacar raiz de listas', resultado)

    def test_raiz_de_menos_dos_entre_tres(self):
        resultado = self.calc.raiz(-2,3)
        self.assertEqual('solo numeros positivos', resultado)
    
    def test_raiz_de_una_letra_entre_tres(self):
        resultado = self.calc.raiz('x',3)
        self.assertEqual('solo se puede sacar raiz de numeros', resultado)

    #termina modulo de raiz

if __name__== '__main__':
    unittest.main()