import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# SETUP: open Chrome browser with settings
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# Make the program to download to folder
download_path = os.getcwd()
prefs = {"download.default_directory": download_path}
chrome_options.add_experimental_option("prefs", prefs)


service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.maximize_window()  # make browser full screen

# LOAD PAGE: open login page
driver.get("https://demoqa.com/login")
wait = WebDriverWait(driver, 10)  # wait up to 10 seconds for elements

# LOGIN: wait for fields, enter details, click login
username_field = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))

username_field.send_keys("Phat97")  # type username
password_field.send_keys("Thinasonke@1997")  # type password
driver.execute_script("arguments[0].click();", login_button)  # click login (JS click)

# WAIT: make sure login is complete (profile page loaded)
wait.until(EC.url_contains("profile"))

# NAVIGATE: click "Elements" section
elements = wait.until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span/div')
))
elements.click()

# REMOVE ADS: delete iframe ads that block clicks
driver.execute_script("""
var ads = document.querySelectorAll('iframe');
for (var i = 0; i < ads.length; i++) {
    ads[i].remove();
}
""")

# TEXT BOX: open Text Box page
text_box = wait.until(EC.element_to_be_clickable((By.ID, "item-0")))
text_box.click()

# FORM: wait for fields and fill in details
fullname_field = wait.until(EC.visibility_of_element_located((By.ID, "userName")))
email_field = wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
current_address_field = wait.until(EC.visibility_of_element_located((By.ID, "currentAddress")))
permanent_address_field = wait.until(EC.visibility_of_element_located((By.ID, "permanentAddress")))

fullname_field.send_keys("John Smith")
email_field.send_keys("john@gmail.com")
current_address_field.send_keys("John Street 100, New York, USA")
permanent_address_field.send_keys("Permanent Address Example")

submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
driver.execute_script("arguments[0].click();", submit_button)  # submit form

# UPLOAD & DOWNLOAD: find menu, scroll, click inner element
upload_download = wait.until(EC.presence_of_element_located((By.ID, "item-7")))
driver.execute_script("arguments[0].scrollIntoView(true);", upload_download)
driver.execute_script("arguments[0].querySelector('span').click();", upload_download)

# WAIT: ensure new page loads (download button appears)
download_button = driver.find_element(By.ID, "downloadButton")
driver.execute_script("arguments[0].click();", download_button)


# END: pause and close browser
input("Press enter to close the browser...")
driver.quit()