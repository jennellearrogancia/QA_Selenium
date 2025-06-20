# main.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from login import perform_login  # ← import your login function

# Helper for visible typing
def type_like_human(driver, element, text, delay=0.2):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Setup
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)

# Step 1: Login using imported login function
dummy_email = "jlozano@gmail.com"
dummy_password = "jnelmagno13"
perform_login(driver, dummy_email, dummy_password)

# Step 2: Logout to start fresh registration
driver.find_element(By.CLASS_NAME, "ico-logout").click()
time.sleep(1)

# Step 3: Register a new user
driver.find_element(By.CLASS_NAME, "ico-login").click()
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

rand = random.randint(1000, 9999)
email = f"jlozano{rand}@gmail.com"
password = "jnelmagno13"

driver.find_element(By.ID, "gender-female").click()
type_like_human(driver, driver.find_element(By.ID, "FirstName"), "Jenel")
type_like_human(driver, driver.find_element(By.ID, "LastName"), "Magno")
type_like_human(driver, driver.find_element(By.ID, "Email"), email)
type_like_human(driver, driver.find_element(By.ID, "Password"), password)
type_like_human(driver, driver.find_element(By.ID, "ConfirmPassword"), password)
driver.find_element(By.ID, "register-button").click()
time.sleep(3)

# Step 4: Continue after registration
driver.find_element(By.CLASS_NAME, "register-continue-button").click()
time.sleep(2)

# Step 5: Screenshot
driver.save_screenshot(f"screenshot_{email}.png")

# Step 6: Save credentials
with open("demowebshop_users.txt", "a") as file:
    file.write(f"Email: {email} | Password: {password}\n")

# Step 7: Navigation
driver.find_element(By.LINK_TEXT, "Books").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "ico-cart").click()
time.sleep(2)

# Step 8: Logout and done
driver.find_element(By.CLASS_NAME, "ico-logout").click()
time.sleep(2)

print(f"✅ Automation complete! Registered new account: {email}")
driver.quit()
