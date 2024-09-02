import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

def test_TitleTest():
    HP = webdriver.Chrome()
    HP.maximize_window()

    HP.get("https://thrivenow.in/nashik-tea-house-qa-12")
    print(HP.title)

    act_title = HP.title
    print(act_title)
    if act_title == "Nashik Tea House QA 1, Bandra Order Online":
        assert True
        HP.close()
    else:
        HP.save_screenshot(".\\Screenshots\\" + "test_TitlePage.png")
        HP.close()
        assert False

def test_OrderPass():
    HP = webdriver.Chrome()
    HP.maximize_window()

    HP.get("https://thrivenow.in/nashik-tea-house-qa-12")
    print(HP.title)

    NavClick = HP.find_element(By.XPATH, "//header/div[1]/div[1]/app-icon[1]/*[1]")
    NavClick.click()
    time.sleep(3)
    LoginClick = HP.find_element(By.XPATH, "//li[contains(text(),'Login')]")
    LoginClick.click()
    time.sleep(3)
    LoginNo = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[1]/input[1]")
    LoginNo.send_keys(9560156556)
    time.sleep(6)
    ContinueCTA = HP.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
    ContinueCTA.click()
    time.sleep(3)
    OTP = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
    OTP.send_keys(999999)
    time.sleep(3)
    SetLocation = HP.find_element(By.XPATH, "//span[contains(text(),'Set Location')]")
    SetLocation.click()
    time.sleep(3)
    SelLocation = HP.find_element(By.XPATH,
                              "//body/jw-modal[@id='chooseFrmSavedAddModal']/div[@id='modal']/div[@id='jwModalBody']/app-saved-addresses[1]/div[1]/ul[1]/li[1]")
    SelLocation.click()
    time.sleep(3)
    #Closewindow = HP.find_element(By.XPATH,
    #                          "//body/jw-modal[@id='outletUpdateModal']/div[@id='modal']/div[@id='jwModalBody']/div[1]/*[1]")
    #Closewindow.click()
    #time.sleep(3)
    #HP.execute_script("window.scrollTo(0, 400);")
    #time.sleep(3)
    VegToggleBtn = HP.find_element(By.XPATH,
                               "//body/app-root[1]/div[1]/app-browse-menu[1]/div[2]/div[3]/div[2]/div[1]/span[1]/label[1]")
    time.sleep(1)
    VegToggleBtn.click()
    time.sleep(1)
    VegToggleBtn.click()
    NonVegToggleBtn = HP.find_element(By.XPATH,
                                  "//body/app-root[1]/div[1]/app-browse-menu[1]/div[2]/div[3]/div[2]/div[1]/span[2]/label[1]")
    NonVegToggleBtn.click()
    time.sleep(1)
    NonVegToggleBtn.click()
    IncludesEggToggleBtn = HP.find_element(By.XPATH,
                                       "//body/app-root[1]/div[1]/app-browse-menu[1]/div[2]/div[3]/div[2]/div[1]/span[3]/label[1]")
    IncludesEggToggleBtn.click()
    time.sleep(1)
    IncludesEggToggleBtn.click()
    time.sleep(2)
    #SearchItm = HP.find_element(By.TAG_NAME, "input")
    #SearchItm.send_keys("Hashbrown")
    #time.sleep(3)
    #SearchItm.clear()
    HP.refresh()
    HP.execute_script("window.scrollTo(0, 400);")
    time.sleep(3)
    SelCategory = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-browse-menu[1]/div[2]/div[3]/div[1]/div[2]")
    SelCategory.click()
    time.sleep(2)
    SelItem1 = HP.find_element(By.XPATH,
                           "//body/app-root[1]/div[1]/app-browse-menu[1]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div[1]/app-menu-item[1]/div[1]/div[2]")
    SelItem1.click()
    time.sleep(2)
    AddItem1 = HP.find_element(By.XPATH, "//div[contains(text(),'ADD ITEM')]")
    AddItem1.click()
    time.sleep(2)
    ViewCart = HP.find_element(By.XPATH, "//body[1]/app-root[1]/div[1]/app-browse-menu[1]/div[3]/div[1]/div[1]/div[1]/div[2]")
    ViewCart.click()
    time.sleep(2)
    AddMoreItem1 = HP.find_element(By.XPATH,
                               "//body/app-root[1]/div[1]/app-your-order[1]/div[1]/div[1]/div[1]/table[1]/tr[1]/td[2]/div[1]/span[2]/app-icon[1]/*[1]")
    AddMoreItem1.click()
    time.sleep(2)
# RemoveOff = HP.find_element(By.XPATH, "//span[contains(text(),'Remove')]")
# RemoveOff.click()
# time.sleep(2)
    ProPay = HP.find_element(By.XPATH,
                         "//body/app-root[1]/div[1]/app-your-order[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]")
    ProPay.click()
    time.sleep(2)
    Netbnk = HP.find_element(By.XPATH, "//div[contains(text(),'Netbanking')]")
    Netbnk.click()
    time.sleep(2)
    SelHDFC = HP.find_element(By.XPATH,
                          "//body/app-root[1]/div[1]/app-your-order[1]/app-payments[1]/div[1]/app-payments-netbanking[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    SelHDFC.click()
    time.sleep(2)
# Failure = HP.find_element(By.XPATH, "//button[contains(text(),'Failure')]")
# Failure.click()
# time.sleep(2)
    SuccessPay = HP.find_element(By.XPATH, "//button[contains(text(),'Success')]")
    SuccessPay.click()
    time.sleep(3)
    TrkBtn = HP.find_element(By.XPATH, "//button[contains(text(),'Track order status')]")

    if TrkBtn.is_displayed():
        TrkBtn.click()
        time.sleep(2)
        GetOrderID = HP.find_element(By.XPATH, "//body/app-root[1]/div[1]/app-track-order[1]/div[1]/div[2]/div[2]")
        print('Order placed successfully', GetOrderID.text)
        time.sleep(2)
        HP.close()
        assert True
    else:
        print("Order Failure")
        time.sleep(2)
        HP.close()
        assert False
