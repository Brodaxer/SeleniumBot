from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# f_name = driver.find_element(By.XPATH, value="/html/body/form/input[1]")
f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email_adress = driver.find_element(By.NAME, value="email")
f_name.send_keys("Bolek")
l_name.send_keys("Lolek")
email_adress.send_keys("bolek.lolek@mail.com")
sign_up = driver.find_element(By.XPATH, value="/html/body/form/button")
sign_up.click()
