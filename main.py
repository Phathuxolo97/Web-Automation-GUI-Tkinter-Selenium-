from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class WebAutomation:
    def __init__(self):
        # SETUP: open Chrome browser with settings
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Make the program to download to folder
        download_path = os.getcwd()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)
        self.driver.maximize_window()  # make browser full screen


    def login(self , username , password):
        # LOAD PAGE: open login page
        self.driver = self.driver
        self.driver.get("https://demoqa.com/login")
        self.wait = WebDriverWait(self.driver, 10)  # wait up to 10 seconds for elements

        # LOGIN: wait for fields, enter details, click login
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login")))

        username_field.send_keys(username)  # type username
        password_field.send_keys(password)  # type password
        self.driver.execute_script("arguments[0].click();", login_button)  # click login (JS click)

    def fill_form(self,fullname , email , currect_address , permanent_address ):
        # WAIT: make sure login is complete (profile page loaded)
        self.wait.until(EC.url_contains("profile"))

        # NAVIGATE: click "Elements" section
        elements = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span/div')
        ))
        elements.click()

        # REMOVE ADS: delete iframe ads that block clicks
        self.driver = self.driver
        self.driver.execute_script("""
        var ads = document.querySelectorAll('iframe');
        for (var i = 0; i < ads.length; i++) {
            ads[i].remove();
        }
        """)

        # TEXT BOX: open Text Box page
        text_box = self.wait.until(EC.element_to_be_clickable((By.ID, "item-0")))
        text_box.click()

        # FORM: wait for fields and fill in details
        fullname_field = self.wait.until(EC.visibility_of_element_located((By.ID, "userName")))
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "userEmail")))
        current_address_field = self.wait.until(EC.visibility_of_element_located((By.ID, "currentAddress")))
        permanent_address_field = self.wait.until(EC.visibility_of_element_located((By.ID, "permanentAddress")))

        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(currect_address)
        permanent_address_field.send_keys(permanent_address)

        submit_button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        self.driver.execute_script("arguments[0].click();", submit_button)  # submit form

    def download_file(self):
        # UPLOAD & DOWNLOAD: find menu, scroll, click inner element
        upload_download = self.wait.until(EC.presence_of_element_located((By.ID, "item-7")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", upload_download)
        self.driver.execute_script("arguments[0].querySelector('span').click();", upload_download)

        # WAIT: ensure new page loads (download button appears)
        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        # close browser
        self.driver.quit()

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login("Phat97" , "Thinasonke@1997")
    webautomation.fill_form("John Smith" , "john@gmail.com", "Street1", "Street2")
    webautomation.download_file()
    webautomation.close()











