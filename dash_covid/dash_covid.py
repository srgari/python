#%%
import pandas as pd
import numpy 
import plotly.offline as po
import plotly.graph_objs as go
from bs4 import BeautifulSoup
import requests
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium import webdriver # start from here
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


site1 = "https://www.python.org/"
site2 = "https://covid.saude.gov.br/"

#%%
driver = webdriver.Firefox() # open the browser
driver.get("https://covid.saude.gov.br/") # open this webpage

print(driver.title)

try: driver.find_element_by_class_name('ion-page')
except: print('damn!')
with open('lala.txt', 'w') as x:
    x.write(driver.page_source)


# driver.find_element_by_class_name('button-inner')
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()

# driver.title
# %%
req = requests.get(site2)
bs = BeautifulSoup(req.text)

re.findall('.......a.....', req.text)
# %%
