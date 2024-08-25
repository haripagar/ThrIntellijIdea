from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

HP = webdriver.Chrome()
HP.maximize_window()

HP.get("https://thrivenow.in/nashik-tea-house-qa-12")
# print(HP.title)

NavClick = HP.find_element(By.XPATH, "//header/div[1]/div[1]/app-icon[1]/*[1]")
NavClick.click()
time.sleep(3)

LoginClick = HP.find_element(By.XPATH, "//li[contains(text(),'Login')]")
LoginClick.click()
time.sleep(3)

SignupNo = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[1]/input[1]")
SignupNo.send_keys(7887721448)
ContinueCTA = HP.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
ContinueCTA.click()
time.sleep(6)

#OTP = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
#OTP.send_keys(0000)
Continue2CTA = HP.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
Continue2CTA.click()
time.sleep(5)

FullName = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-signup[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
FullName.send_keys("Harshal")
Email = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-signup[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
Email.send_keys("hp@gmail.com")
time.sleep(3)

DateSel = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-signup[1]/div[1]/form[1]/div[3]/div[1]/input[1]")
DateSel.click()
DateSel.send_keys(Keys.CONTROL, "a")
DateSel.send_keys(Keys.BACKSPACE)
DateSel.send_keys("22081999")
time.sleep(5)

Continue3CTA = HP.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
Continue3CTA.click()
time.sleep(3)





