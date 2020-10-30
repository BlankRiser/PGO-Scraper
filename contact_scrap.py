from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import time
import pickle

options = webdriver.ChromeOptions()

# Path to chrome profile can be found here- chrome://version/
options.add_argument(
    "user-data-dir=C:/Users/rscho/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(executable_path="chromedriver.exe",
                          options=options)


# Getting contact details using XPath
contacts = []
count = 0
for url in urls:
    print("Url {count}")
    driver.get(url)
    time.sleep(10)
    # pay attention: find_element*s*
    if len(driver.find_elements_by_xpath('//*[@id="btnViewCallNumber"]')) > 0:
        btn = driver.find_element_by_xpath('//*[@id="btnViewCallNumber"]')
        driver.execute_script("arguments[0].click();", btn)
        # btn.click()
        time.sleep(3)
        contact = driver.find_element_by_xpath('//*[@id="revealedMobNum"]')
        if (contact != None):
            contact = contact.text
        contacts.append(contact)
    else:
        contact = "Ad"
        contacts.append(contact)

print(contacts)
