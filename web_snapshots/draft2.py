import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#set the url
url = "https://accounts.google.com/v3/signin/identifier?dsh=S167982485%3A1689331180994684&authuser=0&continue=http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F8494%3Fhl%3Den%26co%3DGENIE.Platform%253DDesktop&ec=GAlAdQ&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession"

# Set the interval between screenshots (in seconds)
interval = 30  # 30 seconds

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)
width = 1920
height = 1080
driver.set_window_size(width, height)

try:
    while True:
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        
        # Refresh the webpage
        driver.refresh()

        # Wait for the page to fully load after refresh
        time.sleep(2)
        
        #saving the screenshort
        driver.save_screenshot(filename)
        print(f"Screenshot captured: {filename}")

        # Wait for the specified interval
        time.sleep(interval)

except KeyboardInterrupt:
    # Press Ctrl+C to stop the program
    driver.quit()

finally:
    driver.quit()
