import os
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
zomato_mumbai_url = "https://www.zomato.com/mumbai/great-food-no-bull"
zomato_bangalore_url="https://www.zomato.com/bangalore/great-food-no-bull"
zomato_pune_url="https://www.zomato.com/pune/great-food-no-bull"

def get_driver():
 chrome_options=Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--headless')
 chrome_options.add_argument('--disable-dev-shm-usgae')
 user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
 chrome_options.add_argument('user-agent=       {0}'.format(user_agent))
 driver = webdriver.Chrome(options=chrome_options)
 return driver

 driver=get_driver()   

def res_name(driver):
   place_divs_tag = 'sc-bke1zw-0'
   places = driver.find_element(By.CLASS_NAME,place_divs_tag)
   tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
   res_names = []
   for i in tags:
    res_names.append(i.find_element(By.XPATH,".//div/section/div[1]/a").text)
   return res_names[:100]

def res_url(driver):
   place_divs_tag = 'sc-bke1zw-0' 
   places = driver.find_element(By.CLASS_NAME,place_divs_tag)
   tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
   urls = []
   for i in tags:
     urls.append(i.find_element(By.TAG_NAME,"a").get_attribute('href'))
   return urls[:100]

def res_ratings(driver):
   place_divs_tag = 'sc-bke1zw-0'
   places = driver.find_element(By.CLASS_NAME,place_divs_tag)
   tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
   ratings = []
   for i in tags:
     try:     ratings.append(i.find_element(By.CLASS_NAME,'sc-1q7bklc-5').text)
     except:
          ratings.append('.')
   return ratings[:100]   

def get_all_cities():
  cities = ['mumbai','bangalore','pune']
 
  dic={'NAME':[],'RATINGS':[],'LINK':[]}  
  for i in cities:
    base_url = 'https://www.zomato.com/'+ i + '/great-food-no-bull'
    driver.get(base_url)
    dic['NAME'].extend(res_name(driver))
    dic['RATINGS'].extend(res_ratings(driver)) 
    dic['LINK'].extend(res_url(driver)) 
  return dic      


if __name__ =="__main__":
  driver = get_driver()
  print('Fetching Best 100 Places For 3 Locations')
  mbp100=get_all_cities()
  print(mbp100)  
  best100df=pd.DataFrame(mbp100)
  best100df.to_csv('best100.csv',index=False)  


  

 
  
    


    
 
        
