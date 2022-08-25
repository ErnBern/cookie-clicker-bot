from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


ser = Service('C:\Program Files (x86)\chromedriver.exe')
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

i = 0

while i == 0:
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
        check = WebDriverWait(driver, 0.001).until(
        EC.presence_of_element_located((By.ID, f'product{buyingProduct + 1}'))
        ).text.split("\n")[0]
        if check != "???":
            buyingProduct += 1
    except:
        pass