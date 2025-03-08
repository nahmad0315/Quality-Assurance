import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome options for headless mode (optional)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment if you don't need the browser UI

# Set up the ChromeDriver service
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Guru99 demo site
driver.get("https://demo.guru99.com/test/newtours/")

# Introduce a random delay to mimic human interaction
time.sleep(random.uniform(3, 5))  # Sleep between 3 and 5 seconds

# You can interact with the page here or just print the title
print(driver.title)

# Wait for the user to manually close the browser
# This prevents the browser from closing automatically
input("Press Enter to close the browser...")

# Close the browser manually
driver.quit()
