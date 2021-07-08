from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "email"
PASSWORD = "password"
webdriver_path = "C:/development/chromedriver.exe"

REPO_NAME = "git_repo_auto"
REPO_DESCRIPTION = "Login and create a repo automatically"

driver = webdriver.Chrome(executable_path=webdriver_path) 
driver.get("https://github.com/")

time.sleep(4)
driver.maximize_window()
sign_in = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a')))
sign_in.click()

####### Credentials: 1. Login #####
time.sleep(5)
username = driver.find_element_by_name('login')
password = driver.find_element_by_name('password')
time.sleep(1)
username.send_keys(EMAIL)
password.send_keys(PASSWORD)
time.sleep(1)
password.send_keys(Keys.ENTER)

##### 2. Create repo #####
time.sleep(3)
new_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="repos-container"]/h2/a'))).click()

repo_name =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="repository_name"]')))
repo_name.send_keys(REPO_NAME)
time.sleep(2)
repo_description =WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="repository_description"]')))
repo_description.send_keys(REPO_DESCRIPTION)
print(driver.current_url)
