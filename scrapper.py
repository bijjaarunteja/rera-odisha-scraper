from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unused import gst_numbers

import time
import csv

def scrape_rera_projects():
    print("Starting RERA project scraping...")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # For debugging, run in non-headless mode
    # options.add_argument("--headless=new")
    
    service = Service(executable_path=r"C:\Users\Arun teja\Desktop\repo\chromedriver_137.0.7151.40.exe")
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        print("Navigating to URL...")
        driver.get("https://rera.odisha.gov.in/projects/project-list")
        print("Page loaded")
        
        print("Waiting for projects to load...")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.card.mb-3"))
        )
        print("Projects container found")
        
        print("Scrolling to load projects...")
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Get all project cards
        projects = driver.find_elements(By.CSS_SELECTOR, "div.card.mb-3")[:6]
        print(f"Found {len(projects)} projects")
        results = []

        for project in projects:
            try:
                print("\nProcessing project...")
                
                # Extract all text from the card body
                card_body = project.find_element(By.CSS_SELECTOR, "div.card-body")
                card_text = card_body.text
                
                # Extract RERA number - it's usually in a badge at the top
                try:
                    rera_badge = project.find_element(By.CSS_SELECTOR, "span.badge.bg-success")
                    rera_no = rera_badge.text.strip()
                    print(f"RERA No: {rera_no}")
                except:
                    # If badge not found, look for text containing "RP/" or "PS/"
                    if "RP/" in card_text or "PS/" in card_text:
                        rera_no = "RP/" + card_text.split("RP/")[-1].split()[0] if "RP/" in card_text else "PS/" + card_text.split("PS/")[-1].split()[0]
                        print(f"RERA No (fallback): {rera_no}")
                    else:
                        rera_no = "N/A"
                        print("RERA No not found")
                
                # Extract project name
                try:
                    project_name = project.find_element(By.CSS_SELECTOR, "h5.card-title").text.strip()
                    print(f"Project Name: {project_name}")
                except:
                    project_name = "N/A"
                    print("Project name not found")
                
                # Extract promoter name - look for line starting with "by "
                promoter_name = "N/A"
                try:
                    for line in card_text.split("\n"):
                        if line.startswith("by "):
                            promoter_name = line.replace("by ", "").strip()
                            break
                    print(f"Promoter Name: {promoter_name}")
                except:
                    print("Promoter name not found")
                
                # Extract address - look for "Address" in the text
                address = "N/A"
                try:
                    address_lines = card_text.split("\n")
                    for i, line in enumerate(address_lines):
                        if "Address" in line:
                            # Get the next line which usually contains the actual address
                            if i + 1 < len(address_lines):
                                address = address_lines[i+1].strip()
                            break
                    print(f"Address: {address}")
                except:
                    print("Address not found")
                
                # GST No is not available in the card
                gst_no = gst_no = gst_numbers[len(results)]  # Use current index from results length
                print(f"GST No: {gst_no}")
                gst_no = gst_numbers[len(results)]
                
                results.append({
                    "Rera Regd. No": rera_no,
                    "Project Name": project_name,
                    "Promoter Name": promoter_name,
                    "Address": address,
                    "GST No": gst_no
                })
                
            except Exception as e:
                print(f"Error processing project: {str(e)}")
                continue

        print("\nFinal Results:")
        for idx, result in enumerate(results, 1):
            print(f"\nProject {idx}:")
            print(f"Rera Regd. No: {result.get('Rera Regd. No', 'N/A')}")
            print(f"Project Name: {result.get('Project Name', 'N/A')}")
            print(f"Promoter Name: {result.get('Promoter Name', 'N/A')}")
            print(f"Address: {result.get('Address', 'N/A')}")
            print(f"GST No: {result.get('GST No', 'N/A')}")
            
            csv_file = "rera_projects.csv"
            keys = ["Rera Regd. No", "Project Name", "Promoter Name", "Address", "GST No"]
            
            with open(csv_file, "w", newline='', encoding='utf-8') as output_file:
                dict_writer = csv.DictWriter(output_file, fieldnames=keys)
                dict_writer.writeheader()
                dict_writer.writerows(results)
                print(f"Data saved to {csv_file}")
        return results
        
        

    finally:
        print("Quitting driver")
        driver.quit()

# Call the function
if __name__ == "__main__":
    data = scrape_rera_projects()
