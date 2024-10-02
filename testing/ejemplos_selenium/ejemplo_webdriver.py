from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class TestPythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()

    def test_tittle_python(self):
        self.driver.get("http://www.python.org")
        self.assertEqual("Python",self.driver.title)

    def test_results_no_found(self):
        busqueda = self.driver.find_element(By.NAME, "q")
        busqueda.clear()
        busqueda.send_keys("pycon" + Keys.RETURN)
        self.assertNotIn("No results found.", self.driver.page_source)

if __name__ == '__main__':
    unittest.main()