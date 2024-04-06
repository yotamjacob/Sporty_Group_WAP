from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import os
from PIL import Image

# Define desired mobile device
mobile_emulation = {
    "deviceName": "iPhone X"
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://m.twitch.tv/')

time.sleep(1)

search_icon = driver.find_element(By.CSS_SELECTOR, 'a[href="/search"]')

search_icon.click()
search_input = driver.find_element(By.CSS_SELECTOR, 'input[type="search"]')
search_input.send_keys("StarCraft II")
search_input.send_keys(Keys.RETURN)

for _ in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  

streamer = driver.find_element(By.CSS_SELECTOR, '.tw-image')
streamer.click()

# Wait for the video element to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'video'))
    )
    time.sleep(5)
except Exception as e:
    print("Error:", e)

driver.save_screenshot("twitch_with_video.png")

driver.quit()