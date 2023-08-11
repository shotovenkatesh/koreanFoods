import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import scrape
import csv

ALL_LINKS = ["beverages", "ready-to-eat", "hot-spicy", "healthy", "cooking-essentials", "snacks-2",
             "covid-19-essentials", "dalgona🍭", "combo-meals", "enjoy-to-cook", "pay-day-sale", ""]

ROW_LIST = [["Title", "Current Price", "Actual Price", "Description","How To","Images"],
             ]

def fetch_data(site,no):
    driver.get(f"https://foodkoreadubai.com/collections/{site}?page={no}")
    box_product_elements = driver.find_elements(By.CSS_SELECTOR, ".box.product")
    i = 1
    last_product = len(box_product_elements)
    while i < last_product:
        driver.find_elements(By.CSS_SELECTOR, ".box.product")[i].click()
        # scrapping is happening here
        url = driver.current_url
        #send the site name to the start scraping method so it adds to that csv file
        scrape.start_scraping(url,site)
        driver.back()
        i += 1
        time.sleep(2)


chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://foodkoreadubai.com/collections/beverages")
time.sleep(10)
try:
    popup_element = driver.find_element(By.CLASS_NAME, "popup-close")
    close_button = popup_element.find_element(By.CSS_SELECTOR, ".icon-close")
    close_button.click()
    time.sleep(4)
except StaleElementReferenceException:
    print("Pop up did not pop up")
finally:
    try:
        next_pages = []
        next_page_exist = driver.find_elements(By.CSS_SELECTOR, ".pagination li a")
        for page in next_page_exist:
            next_pages.append(page.text)
        next_pages.pop(-1)
        next_pages = [int(page) for page in next_pages]
        for site in ALL_LINKS:
            ## creates a new csv file
            with open(f'{site}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(ROW_LIST)
            for no in next_pages:
                fetch_data(site,no)


    except NoSuchElementException:
        print("There is no second page")
