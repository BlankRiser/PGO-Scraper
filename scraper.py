import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
from selenium.webdriver.common.keys import Keys
import json
import re
# import pandas as pd
# import numpy as np


driver = webdriver.Chrome('chromedriver')

scrape_this_url = 'https://www.gopgo.in/bengaluru/pgo-properties'

driver.get(scrape_this_url)
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
    # if i >= 1:
    #     break
    # if i >= 697:  # takes exactly 697 scroll to get complete data
    #     break


soup = BeautifulSoup(driver.page_source, "html.parser")

scripts = []
for tags in soup.find_all('script', type='application/ld+json'):
    # print(tags.string)
    data = json.loads(tags.string)
    scripts.append(data)


# Converting to JSON
print("\n------------------Creating JSON!------------------\n")
with open('data.json', 'w') as f:
    json.dump(scripts, f)
print("\n------------------JSON Made!------------------\n")

print(len(scripts))
