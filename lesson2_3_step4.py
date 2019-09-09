from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector('button[type="submit"]')
	button.click()

	time.sleep(2)

	confirm=browser.switch_to.alert
	confirm.accept()

	time.sleep(2)

	x_element = browser.find_element_by_css_selector("#input_value.nowrap")
	x = x_element.text
	y = calc(x)

	input1 = browser.find_element_by_css_selector("#answer")
	input1.send_keys(y)

	button = browser.find_element_by_xpath('//button[text()="Submit"]')
	button.click()

finally:
	# успеваем скопировать код за 30 секунд
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файл