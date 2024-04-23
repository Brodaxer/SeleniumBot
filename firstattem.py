from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is: {price_dollar.text}.{price_cents.text}")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)
# --------------------------------------

# event_list = {}
# for _ in driver.find_elements(By.CSS_SELECTOR, value="time"):
#     print(_.text)
# news = driver.find_element(By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[2]')
# news2 = news.find_element(By.CLASS_NAME, value='menu')
# new3 = news2.find_element(By.TAG_NAME, value='a')
# new3 = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# def get_date():
#     date_list = []
#     for ele in driver.find_elements(By.CSS_SELECTOR, value="time"):
#         date_list.append(ele.text)
#     return date_list
#
# def get_event_name():
#     event_text = []
#     for ele in news2.find_elements(By.TAG_NAME, value='a'):
#         event_text.append(ele.text)
#     return event_text
#
#
# for x in range(len(get_date())):
#     add = {"time": get_date()[x-1], "name": get_event_name()[x-1]}
#     event_list.update({x: add})
#
# print(event_list)

driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Identify the email text box
email_txt = driver.find_element(By.NAME, "email_input")

# Fetch the value property associated with the textbox
value_info = email_txt.get_attribute("value")
print(value_info)
# driver.quit()