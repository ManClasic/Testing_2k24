from behave import  given, when , then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


@given(u'que ingreso mi usuario "{username}" y contraseña "{password}"')
def step_impl(context, username, password):
    context.driver = webdriver.Chrome()
    context.driver.get('http://localhost:8000/admin')
    context.driver.find_element(By.NAME, 'username').send_keys(username)
    context.driver.find_element(By.NAME, 'password').send_keys(password)


@when(u'presiono el botón Identificarse')
def step_impl(context):
    context.driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
    # context.driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()
    time.sleep(1)


@then(u'puedo ver el mensaje de "{mensaje}"')
def step_impl(context, mensaje):
    mensaje_obtenido = context.driver.find_element(By.ID, 'user-tools').text
    assert mensaje in mensaje_obtenido, \
    f"El mensaje esperado es {mensaje} y el obtenido es {mensaje_obtenido}"
    time.sleep(1)

@then(u'puedo ver el mensaje de error "{mensaje}"')
def step_impl(context, mensaje):
    mensaje_obtenido = context.driver.find_element(By.CLASS_NAME, 'errornote').text
    assert mensaje == mensaje_obtenido, \
    f"El mensaje esperado es {mensaje} y el obtenido es {mensaje_obtenido}"
    time.sleep(1)
