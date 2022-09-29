import time
from selenium import webdriver
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://bank.gov.ua/ua/markets/exchangerates')
driver.maximize_window()

time.sleep(3)
# v1
euro = driver.find_element('xpath', '//tr/td[contains(text(),"EUR")]/parent::tr/td[contains(text(),",")]')
print(euro.text)

# v2
money_list = ["EUR", "USD", "CHF", "JPY", "GBP"]
for element in money_list:
    time.sleep(3)
    xpath_money = f'//tr/td[contains(text(),"{element}")]/parent::tr/td[contains(text(),",")]'
    money = driver.find_element('xpath', xpath_money)
    print(element, money.text)

# v3 pro
money = driver.find_elements('xpath', '//tr/td[contains(@data-label,"Код літерний")]')
values = driver.find_elements('xpath', '//tr/td[contains(text(),",")]')
for i in range(len(values)):
    print(money[i].text, values[i].text)
