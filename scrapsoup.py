import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
from selenium.webdriver.common.keys import Keys
# import pandas as pd
# import numpy as np

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.gopgo.in/bengaluru/pgo-properties')
time.sleep(5)  # Allow 2 seconds for the web page to open
# You can set your own pause time. My laptop is a bit slow so I use 1 sec
scroll_pause_time = 5  # to get more data Default: 1
screen_height = driver.execute_script(
    "return window.screen.height;")   # get the screen height of the web
i = 1  # default:1

while True:
    # scroll one screen height each time
    driver.execute_script(
        "window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    print(i)
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break
    # if i >= 2:
    #     break
    if i >= 697:  # takes exactly 697 scroll to get complete data
        break

content = []
soup = BeautifulSoup(driver.page_source, "html.parser")

for parent in soup.find_all(class_="single-item"):

    name = parent.find("h2", class_="proptery-hostels-name-l-title")
    # urls = [item.get("href") for item in soup.find_all("a")]
    link = parent.find("a")
    print(type(link))
    address = parent.find("div", class_="proptery-hostels-p")
    day_rent = parent.find("p", class_="property-card-col__daily")
    month_rent = parent.find("p", class_="property-card-col__monthly")

    if name != None:
        name = name.text
    if link != None:
        url = 'https://www.gopgo.in/' + link["href"]

    if address != None:
        address = address.text
    if day_rent != None:
        day_rent = day_rent.text
    if month_rent != None:
        month_rent = month_rent.text

    content.append(
        {'name': name, 'address': address,
         'day_rent': day_rent, 'month_rent': month_rent, 'url': url}
    )

print("------------------Making CSV!------------------")
with open("data.csv", "w", newline="") as csv_file:
    cols = ["name", "address", "day_rent", "month_rent", "url"]
    writer = csv.DictWriter(csv_file, fieldnames=cols)
    writer.writeheader()
    writer.writerows(content)

print("\n------------------CSV Made!------------------\n")
print(len(content))
