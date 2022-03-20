"""
This script coded by github.com/OmarAEH
Feel free to contact me at anytime.
"""

import linecache
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Do not wait for full page load
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

# Get Number of Links in links file
with open('Links.txt') as f:
    text = f.readlines()
    size = len(text)

numberOfLinks = size
count = 1


# Open all links
for link in range(1, int(numberOfLinks + 1)):

    # Open 30 tabs change the 30 number to change the tabs number
    for tab in range(0, 30):
        # Open 30 tabs change the 30 number to change the tabs number
        current_link = linecache.getline("Links.txt", count)
        current_link = current_link.rstrip()
        if count % 30:
            # Open link in new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[tab])
            driver.get(current_link)
            # add on to count
            count += 1
        else:
            # Open link in new tab to not waste the 10th link
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[tab])
            driver.get(current_link)
            print(str(count) + " Links Done of : " + str(numberOfLinks))
            input("Press Enter to continue...")
            driver.close()
            driver = webdriver.Chrome(executable_path='chromedriver')
            driver.maximize_window()
            # reset the count
            count += 1
