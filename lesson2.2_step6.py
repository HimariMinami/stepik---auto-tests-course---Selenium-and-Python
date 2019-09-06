from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector("#input_value.nowrap")
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element_by_css_selector("#answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
	input1.send_keys(y)

	label1 = browser.find_element_by_css_selector("#robotCheckbox")
	label1.click()
	label2 = browser.find_element_by_css_selector("#robotsRule")
	label2.click()

	button = browser.find_element_by_tag_name("button")
	button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл