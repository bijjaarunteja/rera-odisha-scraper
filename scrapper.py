from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome driver (make sure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Open the project list page
driver.get("https://rera.odisha.gov.in/projects/project-list")

time.sleep(5)  # wait for page to load fully

# TODO: Add code here to find the first 6 projects and click 'View Details'

# Remember to close the driver at the end
driver.quit()