from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for user to scan the QR code
time.sleep(15)

# Locate the group chat
group_title = "Vaanga Palagalam..."
search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(group_title)
search_box.send_keys(Keys.ENTER)

# Simulate typing
input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
input_box.send_keys("Typing...")

# Keep the typing status active
while True:
    time.sleep(2)
    input_box.send_keys(Keys.BACKSPACE)
    input_box.send_keys("Typing...")
