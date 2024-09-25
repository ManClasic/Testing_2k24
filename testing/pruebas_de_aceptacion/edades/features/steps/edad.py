from behave import given, when, then
from edades import Edades

@given(u'que ingreso al sistema la edad de "{numero}"')
def step_impl(context, numero):
    context.numero = int(numero)

@given(u'que ingreso al sistema el caracter "{caracter}"')
def step_impl(context, caracter):
    context.numero = caracter


@when(u'presiono el botón Mensaje')
def step_impl(context):
    edades = Edades()
    context.mensaje = edades.calc_edad(context.numero)
   

@then(u'puedo ver el mensaje "{mensaje_esperado}"')
def step_impl(context, mensaje_esperado):
    assert mensaje_esperado == context.mensaje, \
        f"El mensaje esperado es {mensaje_esperado} y el obtenido es {context.mensaje}"