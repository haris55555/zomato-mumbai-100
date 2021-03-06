import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
zomato_mumbai_url = "https://www.zomato.com/mumbai/great-food-no-bull"

def get_driver():
 chrome_options=Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--headless')
 chrome_options.add_argument('--disable-dev-shm-usgae')
 user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
 chrome_options.add_argument('user-agent=       {0}'.format(user_agent))
 driver = webdriver.Chrome(options=chrome_options)
 return driver

def get_places(driver):
  place_divs_tag = 'sc-bke1zw-0'
  driver.get(zomato_mumbai_url)
  time.sleep(5)
  places = driver.find_element(By.CLASS_NAME,place_divs_tag)
  tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
  return tags[:100]
    
if __name__ =="__main__":
  driver = get_driver()
  print('fetching lists')
  x = get_places(driver)
  print(len(x))

  print('parsing the place')
# NAME,ratings,link 
  places=get_places(driver)     
  place=places[0]
  hotel =[]
  ratings =[]  
  link = []  
  for i in places:
      try:
        ratings.append(i.find_element(By.CLASS_NAME,'sc-1q7bklc-5').text) 
        link.append(i.find_element(By.TAG_NAME,'a').get_attribute('href'))
      except:
        ratings.append('')
        link.append('')
  for place in places: 
        hotel.append(place.find_element(By.XPATH,'.//div/section/div[1]/a').text) 
        
#ratings[:100].append(place.find_element(By.CLASS_NAME,'sc-1q7bklc-5').text) 
        #except NoSuchElementException:
        
        print('NAME:',hotel[:100])  
        print(len(hotel))
        print('Ratings:', ratings[:100])
        print(len(ratings))
        print('URL:',link[:100])
        print(len(link))