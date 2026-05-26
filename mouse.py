#!/usr/bin/env python3

import os
import sys
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Check that the required argument has been passed
if len(sys.argv) < 2 or sys.argv[1] not in ["Performance", "Powersave"]:
    print(f"USAGE: {sys.argv[0]} [Performance|Powersave]")
    sys.exit(1)

# Store the first command line argument
MODE = sys.argv[1]

# Store the URL to visit
URL = "https://www.mchose.com.cn/#/detail?deviceName=MCHOSE+A7+V2+Ultra"

# Path to the user's home directory
HOME = os.path.expanduser("~")

# Path to the Chrome user profile for persistent session
CHROME_PROFILE_PATH = f"{HOME}/.config/chromium_profile"

# Initialize Chrome options object
options = Options()

# Set the path to the Chrome user data directory, so Chrome uses this profile's data
options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")

# Set up Chrome options
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")

try:
    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=options)
    
    # Open the specified URL
    driver.get(URL)
    
    # Wait up to 15 seconds for the element matching MODE text to be clickable
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, f"//*[normalize-space()='{MODE}']"))
    )
    
    # Click the element once it is clickable
    element.click()
    
finally:    
    # Quit the browser and clean up resources
    driver.quit()
    
    # Capture additional Steam commands
    cmd = sys.argv[2:]
    
    # Run the external commands
    subprocess.run(cmd)
