from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Use full path to chromedriver.exe
service = Service("C:/Users/Arun teja/Desktop/repo/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
time.sleep(3)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("OpenAI ChatGPT")
search_box.submit()

time.sleep(20)
driver.quit()
