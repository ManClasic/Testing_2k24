from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from credenciales import usuario, password

driver = webdriver.Chrome()

driver.get(
    "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=161&ct=1727832317&rver=7.5.2211.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26culture%3des-mx%26country%3dmx%26RpsCsrfState%3d188fb75a-32c7-c6b7-fb2e-913f400561a2&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c")
time.sleep(1)
driver.find_element(By.NAME, "loginfmt").send_keys(usuario + Keys.RETURN)

time.sleep(1)
driver.find_element(By.NAME, "passwd").send_keys(password + Keys.RETURN)

time.sleep(1)
driver.find_element(By.ID, "acceptButton").click()

time.sleep(5) 

driver.quit()