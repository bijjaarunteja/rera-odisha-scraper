from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com")
data = []

while True:
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for q in quotes:
        text = q.find_element(By.CLASS_NAME, "text").text
        author = q.find_element(By.CLASS_NAME, "author").text
        tags = q.find_element(By.CLASS_NAME, "tags").text
        data.append({"Quote": text, "Author": author, "Tags": tags})

    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        next_button.click()
        time.sleep(1)
    except:
        break

df = pd.DataFrame(data)
df.to_csv("all_quotes.csv", index=False)
driver.quit()
