from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
	browser = webdriver.Chrome()

	browser.get("http://suninjuly.github.io/wait2.html")

	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	button = WebDriverWait(browser, 5).until(
        	EC.element_to_be_clickable((By.ID, "verify"))
    	)
	button.click()
	message = browser.find_element_by_id("verify_message")

	assert "successful" in message.text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл