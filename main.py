from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Helper Function: Type like a human with scroll into view
def type_like_human(driver, element, text, delay=0.2):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Setup WebDriver
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)

# Step 1: Click Login
driver.find_element(By.CLASS_NAME, "ico-login").click()
time.sleep(2)

# Step 2: Click Register
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

# Step 3: Fill Registration Form
rand = random.randint(1000, 9999)
email = f"jennellearrogancia47@gmail.com"
password = "jnelmagno13"

driver.find_element(By.ID, "gender-female").click()
type_like_human(driver, driver.find_element(By.ID, "FirstName"), "Jennelle")
type_like_human(driver, driver.find_element(By.ID, "LastName"), "Arrogancia")
type_like_human(driver, driver.find_element(By.ID, "Email"), email)
type_like_human(driver, driver.find_element(By.ID, "Password"), password)
type_like_human(driver, driver.find_element(By.ID, "ConfirmPassword"), password)

# Click Register
driver.find_element(By.ID, "register-button").click()
time.sleep(3)

# Step 4: Click Continue
driver.find_element(By.CLASS_NAME, "register-continue-button").click()
time.sleep(2)

# Step 5: Screenshot after login
driver.save_screenshot(f"screenshot_{email}.png")

# Step 6: Save Account Info
with open("demowebshop_users.txt", "a") as file:
    file.write(f"Email: {email} | Password: {password}\n")

# Step 7: Navigate to Books
driver.find_element(By.LINK_TEXT, "Books").click()
time.sleep(2)

# Step 8: Navigate to Cart
driver.find_element(By.CLASS_NAME, "ico-cart").click()
time.sleep(2)

# Step 9: Logout
driver.find_element(By.CLASS_NAME, "ico-logout").click()
time.sleep(2)

print(f"✅ Automation Success! Account created: {email}")
driver.quit()
