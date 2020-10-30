# PGO Scraper

### Tools reqired

- python 3.8+
- Visual Studio Code

### Prerequisites

1. Make sure you have already logged into [gopgo](https://www.gopgo.in/)

2. Download appropriate version of Chrome driver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).

   - You can find out your chrome version in Chrome's about page or from [here](chrome://settings/help)
   - If your Chrome version is 86.0.+ then only download ChromeDriver 86.0.+
   - Extract the ChromeDriver in the current directory as python code and rename it to `chromedriver.exe`

3. Install python dependencies - Open terminal in the current directory and enter the command below:<br/>
   ```pip install -r requirements.txt```

### How to scrape

- Go to [GOPGO](https://www.gopgo.in/) and select any city and Copy the url
- Open <strong>scraper.py</strong> and find `scrape_this_url`
- Paste the url within inverted quotes after the equals sign besides `scrape_this_url` variable
- Save <strong>scraper.py</strong> after making changes
- Double click <strong>scraper.py</strong> file and wait for a while till you get the message: 'JSON Made!'
- After completion, you can see a `data.json` in the same directory as `scraper.py`
- Go to [convertcsv.com](https://www.convertcsv.com/json-to-csv.htm) and upload `data.json` file and convert it to CSV and Excel formats


### Data Pre-processing using Excel

1. Make sure you have enabled `Developers` tab on your Ms Excel

   - Go to `File -> Options -> Customize Ribbon
   - Tick the `Developer` option in `Main Tabs` on the right and click `Ok` button

2. Formatting the column `@url` to be a valid link
   - Select the column `@url` and go to Developer's tab and click Visual Basic
   - In menu bar, go to `Insert` and click `Module`
   - Copy the code below and press `F5` to run this macro code
   ```
   Sub AppendToExistingOnLeft()
   Dim c As Range
   For Each c In Selection
   If c.Value <> "" Then c.Value = "https://www.gopgo.in" & c.Value
   Next
   End Sub
   ```
   - Now, you can visit the link in column `@url`


### How to use GeoData in Google Maps (Longitude and Latitude)

You can either directly search the longitude and latitude in the map or just use the link below and change the placeholders of <latitude> and <longitude> with actual values:

```
https://www.google.com/maps?q=<latitude>,<longitude>
```

Example: <strong>Hotel Darshan</strong> has Latitude= 15.271669 and Longitude=73.970421 , this is how its [link](https://www.google.com/maps?q=15.271669,73.970421) would look like:<br/>
```https://www.google.com/maps?q=15.271669,73.970421```

### Configure Chrome profile in python

- Find the path to your profile. You can do that by typing `Chrome://version/` in Chrome and copying the profile path. The path should look like this:<br/>
  ```C:\Users\<User Name>\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default```
- Remove Default, we don't need that directory
- When initializinf selenium driver pass this as an argument to the options
- This is how the code with a chrome profile would look like:
```python
from selenium import webdriver
options = webdriver.ChromeOptions()

# Path to chrome profile can be found at- chrome://version/
options.add_argument(
    "user-data-dir=C:/Users/rscho/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(executable_path="chromedriver.exe",
                          options=options)
```
