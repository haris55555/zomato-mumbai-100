from selenium import webdriver
from selenium.webdriver.chrome.options import Options

zomato_mumbai_url = "https://www.zomato.com/mumbai/great-food-no-bull"

chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usgae')
driver = webdriver.chrome(options=chrome_options)

driver.get(zomato_mumbai_url)

print('page',driver.title)