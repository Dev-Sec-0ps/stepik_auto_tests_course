import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait1.html")

    browser.find_element(By.ID, "verify").click()
    msg = browser.find_element(By.ID, "verify_message").text
    assert "Verification was successful!" == msg, "NE TO"

finally:
    print("Verification was successful!")
    browser.quit()
