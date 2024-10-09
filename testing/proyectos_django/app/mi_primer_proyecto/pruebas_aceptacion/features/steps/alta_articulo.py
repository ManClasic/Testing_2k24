from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'entro a la página de registro de artículos')
def step_impl(context):
    context.driver.get('http://localhost:8000/articulos/nuevo')


@given(u'registro el artículo con nombre "{nombre}", con el precio "{precio}"')
def step_impl(context, nombre, precio):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    context.driver.find_element(By.NAME, 'precio').send_keys(precio)


@given(u'descripción "{descripcion}" y en stock "{stock}" unidades.')
def step_impl(context, descripcion, stock):
    context.driver.find_element(By.NAME, 'descripcion').send_keys(descripcion)
    context.driver.find_element(By.NAME, 'stock').send_keys(stock)



@when(u'presiono el botón Agregar')
def step_impl(context):
    context.driver.find_element(By.ID, 'btnAgregar').click()

    


@then(u'puedo ver el artículo "{articulo}" en la lista de artículos.')
def step_impl(context, articulo):
    pass