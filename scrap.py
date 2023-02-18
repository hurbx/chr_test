import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php')
driver.maximize_window()


selection = driver.find_element("xpath", "//select[@name='pagina_offset']")
len_array = driver.find_elements(by=By.TAG_NAME, value='option')
count = 1
for i in range(len(len_array)):
    print(i)
    selection = driver.find_element("xpath", "//select[@name='pagina_offset']")
    drop = Select(selection)
    drop.select_by_visible_text(str(count))
    count += 1
    time.sleep(2)


