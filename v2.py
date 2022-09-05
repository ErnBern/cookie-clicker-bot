from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

ser = Service('Enter Your Chjromedriver Path')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://orteil.dashnet.org/cookieclicker")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'langSelect-EN'))
    )
    element.click()
except:
    pass

buyingProduct = 0

level = int(input("What level do you want to product to be before upgrading?\n"))

i = 0

if level < 100:
    time.sleep(1)
    while i < level * 10:
        time.sleep(0.01)
        driver.find_element(By.ID, 'bigCookie').click()
        i += 1
    print(i)

while i == level * 10:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'bigCookie'))
    ).click()

    e = 0

    while e < 10:
        driver.find_element(By.ID, 'bigCookie').click()
        e += 1
    e = 0

    try:
        cookieAmount = int(str(driver.find_element(By.ID, "cookies").text.split("\n")[0]).split(' ')[0])
    except:
        cookieAmount = int(''.join(str(driver.find_element(By.ID, "cookies").text.split("\n")[0]).split(' ')[0].split(',')))

    try:
        upgrade = WebDriverWait(driver, 0.001).until(
        EC.presence_of_element_located((By.ID, f'product{buyingProduct}'))
        )
        info = upgrade.text.split("\n")
        try:
            price = int(str(info[1]))
        except:
            price = int(''.join(str(info[1]).split(",")))
    except:
        pass

    if cookieAmount == price or cookieAmount > price:
        upgrade.click()

    try:
        upgrades = WebDriverWait(driver, 0.001).until(
        EC.presence_of_element_located((By.ID, f'upgrade0'))
        )
        noUpgrade = False
    except:
        noUpgrade = True

    if noUpgrade == False:
       try:
           upgrades.click()
       except:
            pass  
    try:
        try:
            check = int(str(info[2]))
        except:
            check = int(''.join(str(info[2]).split(",")))
        if check == level:
            buyingProduct += 1
    except: pass
