import time
from selenium import webdriver
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains

# import KEYS
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html')
# driver.set_window_position(1900,300)
driver.maximize_window()

xpath_q1 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1 = driver.find_element('xpath', xpath_q1)
q1.send_keys('M')


xpath_q2 = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[3]/td[3]/input'
q2 = driver.find_element('xpath', xpath_q2)
q2.send_keys(15)


xpath_q9_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
q9_a = driver.find_element('xpath', xpath_q9_a)
q9_a.click()

xpath_q19_a = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
q19_a = driver.find_element('xpath', xpath_q19_a)
q19_a.click()
# time.sleep(2)
# q19_a.click()

xpath_finish = '/html/body/div/div/div/main/div[4]/div[2]/div/form/div/p[1]/input[1]'
xpath_finish_area = '/html/body/div/div/div/main/div[4]/div[2]/div/form/div/p[2]/textarea'
finish = driver.find_element('xpath', xpath_finish)
finish.click()

action = ActionChains(driver)



finish_area = driver.find_element('xpath', xpath_finish_area)
finish_area.click()
#
# # perform the operation
# action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
# action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
#
# from tkinter import Tk
#
# print(Tk().clipboard_get())

#9b /html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[3]/input
#   /html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[3]/div/input

#//input[@name="q9"][@value="b"]


#//input[@name="q9" and @value="b"]

# https://www.selenium.dev/documentation/webdriver/elements/locators/
# https://bank.gov.ua/ua/markets/exchangerates

#XPath axis / оси XPath
#//tr/td[contains(text(),"EUR")]/following::td[3]