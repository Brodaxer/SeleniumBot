import time

from selenium import webdriver
from selenium.webdriver.common.by import By

timeout = time.time() + 60 * 5
five_sec = time.time() + 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")
cash = driver.find_element(By.ID, value="money")

list_of_upgrades = []

def initialize_up_list():
    # for id_name, moni in zip(store.find_elements(By.TAG_NAME, value='div'), store.find_elements(By.TAG_NAME, value="b")):
    for id_name in store.find_elements(By.TAG_NAME, value='div'):
        list_of_upgrades.append(id_name.get_attribute("id"))


initialize_up_list()
list_of_upgrades.pop()
while True:
    click_cookie.click()
    time.sleep(0.1)
    if time.time() > five_sec:
        cash1 = int(cash.text.replace(",", ""))
        for ele in reversed(list_of_upgrades):
            upgrade_cost = int(driver.find_element(By.ID, value=ele).find_element(By.TAG_NAME, value='b').text.split()[-1].replace(",", ""))
            if cash1 >= upgrade_cost:
                driver.find_element(By.ID, value=ele).click()
                break
    test = 0
    click_cookie.click()
    if test == 5 or time.time() > timeout:
        print(driver.find_element(By.ID, value="cps").text)
        break
    test = test - 1
    click_cookie.click()



driver.quit()
