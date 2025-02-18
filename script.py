from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
EMAIL_ID = 'indulekha603@gmail.com'
PASSWORD = 'Testindu@1234'

try:
    # Open Google
    driver.get("https://www.google.com")

    # Find search box and search for "SalesBlink.io"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("SalesBlink.io")
    search_box.send_keys(Keys.RETURN)

    # Wait for CAPTCHA and allow manual intervention
    print("Please solve the CAPTCHA manually and verify images if prompted.")
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "//h3")))  # Adjust wait time as needed

    # After CAPTCHA is solved, wait for results to load
    first_result = driver.find_element("xpath", "//h3")
    print(f"First result: {first_result.text}")
    first_result.click()
    print(f"Navigating to Salesblink.io")

    # Click on Login button
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/nav/div/div[2]/div[2]/ul/li[4]/a"))
    )
    login_button.click()

    # Wait for the login form to appear and enter credentials
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys(EMAIL_ID)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD)

    # Click login button
    login_submit_button = driver.find_element(By.TAG_NAME, "BUTTON")
    login_submit_button.click()

    print(f"Login Successful")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()
