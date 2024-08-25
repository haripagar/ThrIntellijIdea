from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

HP = webdriver.Chrome()
HP.maximize_window()

HP.get("https://thrivenow.in/nashik-tea-house-qa-12/track-order/66924628")
print(HP.title)
time.sleep(2)

# GetOrderID = HP.find_element(By.XPATH, "//span[contains(text(),'66924628')]")

GetOrderID = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-track-order[1]/div[1]/div[2]/div[2]")
print('Order placed successfully', GetOrderID.text)
time.sleep(2)

