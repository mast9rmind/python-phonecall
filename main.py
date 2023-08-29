from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from send_sms import send_sms
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Add this line to run in headless mode
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')  # Required for Docker

def get_page_text(driver, url):
    driver.get(url)
    
    classToSelect = "ctl01_ctl00_NewsList"
    
    try:
        els = driver.find_element(by=By.ID, value=classToSelect)
        return els.text
        
    except Exception as e:
        print(e)
        return None

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.sanjesh.org/fa-IR/sanjesh/4925/page/%DA%A9%D8%A7%D8%B1%D8%B4%D9%86%D8%A7%D8%B3%DB%8C-%D8%A7%D8%B1%D8%B4%D8%AF-"

# Initial request and response
initial_response = get_page_text(driver, url)

while True:
    time.sleep(60)  # Wait for a minute
    
    # Retry and compare response
    retry_response = get_page_text(driver, url)
    
    if retry_response is not None:
        if retry_response == initial_response:
            print("Response is the same as the initial response.")
        else:
            send_sms('OOMAD')
            print("Response has changed from the initial response.")
    else:
        print("Retrying...")
        
driver.quit()
