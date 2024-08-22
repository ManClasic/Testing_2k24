
# DocTest

#primer prueba
'''
>>> sumar(2,3)
5

>>> sumar(3,3)
6

>>> sumar(0,3)
3

>>> sumar(-2,3)
'solo numeros positivos'

>>> sumar('x',3)
'solo se pueden sumar numeros'


>>> sumar(3.5,3)
'solo se pueden sumar numeros enteros'


>>> sumar(3,3.5)
'solo se pueden sumar numeros enteros'
'''

class Calculadora:

    def sumar(self,a,b):
        try:
            if(type(a) == float or type(b) == float):
                return 'solo se pueden sumar numeros enteros'
            if(a < 0 or b < 0):
                return 'solo numeros positivos'
            if(a == None or b == None):
                return 'operacion incompleta'
            if(isinstance(a,list) or isinstance(b,list)):
                return 'no se pueden sumar listas'
            return a + b
        except:
            return 'solo se pueden sumar numeros'
        
    def restar(self,a,b):
        try:
            if(type(a) == float or type(b) == float):
                return 'solo se pueden restar numeros enteros'
            if(a == None or b == None):
                return 'operacion incompleta'
            if(isinstance(a,list) or isinstance(b,list)):
                return 'no se pueden restar listas'
            if(a < 0 or b < 0):
                return 'solo numeros positivos'
            return a- b
        except:
            return 'solo se pueden restar numeros'
        
    def multiplicar(self,a,b):
        try:
            if(type(a) == float or type(b) == float):
                return 'solo se pueden multiplicar numeros enteros'
            if(a == None or b == None):
                return 'operacion incompleta'
            if(isinstance(a,list) or isinstance(b,list)):
                return 'no se pueden multiplicar listas'
            if(a < 0 or b < 0):
                return 'solo numeros positivos'
            return a * b
        except:
            return 'solo se pueden multiplicar numeros'
        
    def dividir(self,a,b):
        try:
            if(type(a) == float or type(b) == float):
                return 'solo se pueden dividir numeros enteros'
            if(a == None or b == None):
                return 'operacion incompleta'
            if(isinstance(a,list) or isinstance(b,list)):
                return 'no se pueden dividir listas'
            if(a < 0 or b < 0):
                return 'solo numeros positivos'
            if(b == 0):
                return 'como vas a dividir entre cero papito...'
            return a / b
        except:
            return 'solo se pueden dividir numeros'
        
    def elevar(self,a,b):
        try:
            if(type(a) == float or type(b) == float):
                return 'solo se pueden elevar numeros enteros'
            if(a == None or b == None):
                return 'operacion incompleta'
            if(isinstance(a,list) or isinstance(b,list)):
                return 'no se pueden elevar listas'
            if(a < 0 or b < 0):
                return 'solo numeros positivos'
            return pow(a,b)
        except:
            return 'solo se pueden elevar numeros'
        
    def raiz(self,a,b):
        try:     
            if(type(a) == float or type(b) == float):
                return 'solo se puede sacar raiz de numeros enteros'
            if(a == None or b == None):
                return 'operacion incompleta'
            if(isinstance(a,list) or isinstance(b,list)):
                return 'no se puede sacar raiz de listas'
            if(a < 0 or b < 0):
                return 'solo numeros positivos'
            return a ** (1/b)
        except:
            return 'solo se puede sacar raiz de numeros'