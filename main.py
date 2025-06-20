from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from login import perform_login  # Reusing login logic

# Helper for visible typing
def type_like_human(driver, element, text, delay=0.2):
    #driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

# Setup
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(2)

# Step 1: Go to Register page
driver.find_element(By.CLASS_NAME, "ico-login").click()
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(2)

# Step 2: Fill registration form
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

# Step 3: Save credentials
with open("demowebshop_users.txt", "a") as file:
    file.write(f"Email: {email} | Password: {password}\n")

# Step 4: Logout after registration
driver.find_element(By.CLASS_NAME, "register-continue-button").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "ico-logout").click()
time.sleep(1)

# Step 5: Login using the newly created account
perform_login(driver, email, password)

# Step 6: Navigate through the site
driver.find_element(By.LINK_TEXT, "Books").click()
time.sleep(2)

# Example: Add first book to cart
driver.find_element(By.CSS_SELECTOR, ".product-item .product-box-add-to-cart-button").click()
time.sleep(2)

# Wait for bar notification to disappear before clicking cart
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "bar-notification"))
)
driver.find_element(By.CLASS_NAME, "ico-cart").click()


# Screenshot
driver.save_screenshot(f"screenshot_{email}.png")

# Step 7: Logout and done
driver.find_element(By.CLASS_NAME, "ico-logout").click()
time.sleep(2)

print(f"✅ Automation complete! Registered and logged in with: {email}")
driver.quit()
