import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_correct_answer(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.implicitly_wait(20)
    browser.get(link)
    answer = str(math.log(int(time.time())))
    #time.sleep(15)
    #input1 = WebDriverWait(browser, 15).until(
    #       EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
    #    )
    input1 = browser.find_element_by_css_selector(".textarea")
    input1.send_keys(answer)
    #button1 = WebDriverWait(browser, 15).until(
    #       EC.visibility_of_element_located((By.CSS_SELECTOR, ".button"))
    #    )
    #time.sleep(5)
    button1 = browser.find_element_by_xpath("//button")
    button1.click()
    #time.sleep(1)
    feedback = browser.find_element_by_css_selector(".smart-hints__hint")
    feedback_text = feedback.text
    assert "Correct!" == feedback_text