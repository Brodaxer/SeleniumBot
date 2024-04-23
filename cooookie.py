from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

timeout = time.time() + 60*1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

click_cookie = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")
monis = store.find_elements(By.TAG_NAME, value="b")
cash = driver.find_element(By.ID, value="money")

upgrades_list = []
def check_for_upgrades():
    for id_name, moni in zip(store.find_elements(By.TAG_NAME, value='div'), monis):
        if len(moni.text.split()) > 0:
            mon = moni.text.split()[-1].replace(",", "")
            id = id_name.get_attribute("id")
            # print(f"{id}-{mon}")
            upgrades_list.append({id: int(mon)})





def cash_status():
    cash1 = int(cash.text.replace(",", ""))
    for ele in upgrades_list:
        for x in ele:
            if cash1 > ele[x]:
                print(f"up available {cash1} ")
            else:
                print(f"nope {cash1} need {ele[x]}")


while True:
    time.sleep(0.5)
    check_for_upgrades()
    upgrades_list.reverse()
    cash_status()
    test = 0
    if test == 5 or time.time() > timeout:
        break
    test = test -1
    click_cookie.click()


driver.quit()