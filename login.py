# login.py

import time
from selenium.webdriver.common.by import By

# Reusable login function
def perform_login(driver, email, password):
    """
    Logs in to Demo Web Shop using visible typing and clicks 'Remember Me'.
    """
    driver.find_element(By.CLASS_NAME, "ico-login").click()
    time.sleep(2)

    email_input = driver.find_element(By.ID, "Email")
    password_input = driver.find_element(By.ID, "Password")
    remember_checkbox = driver.find_element(By.ID, "RememberMe")

    # Type slowly
    for char in email:
        email_input.send_keys(char)
        time.sleep(0.15)

    for char in password:
        password_input.send_keys(char)
        time.sleep(0.15)

    # Click 'Remember Me'
    driver.execute_script("arguments[0].scrollIntoView(true);", remember_checkbox)
    remember_checkbox.click()
    time.sleep(1)

    # Click Login
    driver.find_element(By.XPATH, "//input[@value='Log in']").click()
    time.sleep(2)
