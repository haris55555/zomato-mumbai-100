import smtplib
import os
import json
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

def get_places(driver):
  place_divs_tag = 'sc-bke1zw-0'
  driver.get(zomato_mumbai_url)
  time.sleep(5)
  places = driver.find_element(By.CLASS_NAME,place_divs_tag)
  tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
  return tags[:100]
def parse_mumbai():
  places=get_places(driver)     
  hotel =[]
  ratings =[]  
  link = []   
  for i in places:
    try:
        ratings.append(i.find_element(By.CLASS_NAME,'sc-1q7bklc-5').text) 
        link.append(i.find_element(By.TAG_NAME,'a').get_attribute('href'))
        hotel.append(i.find_element(By.XPATH,'.//div/section/div[1]/a').text)
        
    except:
        ratings.append('.')
        link.append('.')
        hotel.append('.')
    
  return {
            'NAME':hotel[:100],
            'RATINGS':ratings[:100],
            'LINK':link[:100]
         }  
def get_places1(driver):
  place_divs_tag = 'sc-bke1zw-0'
  driver.get(zomato_bangalore_url)
  time.sleep(5)
  places = driver.find_element(By.CLASS_NAME,place_divs_tag)
  tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
  return tags[:100]  

def parse_bangalore():
  places=get_places1(driver)     
  hotel =[]
  ratings =[]  
  link = []   
  for i in places:
    try:
        ratings.append(i.find_element(By.CLASS_NAME,'sc-1q7bklc-5').text) 
        link.append(i.find_element(By.TAG_NAME,'a').get_attribute('href'))
        hotel.append(i.find_element(By.XPATH,'.//div/section/div[1]/a').text)
        
    except:
        ratings.append('.')
        link.append('.')
        hotel.append('.')
    
  return {
            'NAME':hotel[:100],
            'RATINGS':ratings[:100],
            'LINK':link[:100]
         }      
def get_places2(driver):
  place_divs_tag = 'sc-bke1zw-0'
  driver.get(zomato_pune_url)
  time.sleep(5)
  places = driver.find_element(By.CLASS_NAME,place_divs_tag)
  tags=places.find_elements(By.CLASS_NAME,'sc-bke1zw-1')
  return tags[:100]     

def parse_pune():
  places=get_places2(driver)     
  hotel =[]
  ratings =[]  
  link = []   
  for i in places:
    try:
        ratings.append(i.find_element(By.CLASS_NAME,'sc-1q7bklc-5').text) 
        link.append(i.find_element(By.TAG_NAME,'a').get_attribute('href'))
        hotel.append(i.find_element(By.XPATH,'.//div/section/div[1]/a').text)
        
    except:
        ratings.append('.')
        link.append('.')
        hotel.append('.')
    
  return {
            'NAME':hotel[:100],
            'RATINGS':ratings[:100],
            'LINK':link[:100]
         }          
  
if __name__ =="__main__":
  driver = get_driver()
  print('fetching top 100 places')
  x=get_places(driver)
  print(len(x))
  y=get_places(driver)
  print(len(y))
  z=get_places2(driver)  
  print(len(z))  
#assigning variables to get seperate list of name,ratings,links for mum-bang-pune 
  mumbai100=parse_mumbai()
  print(mumbai100)  
  bangalore100=parse_bangalore()
  print(bangalore100)  
  pune100=parse_pune()
  print(pune100)  
  #saving files to_csv
  mumbaidf= pd.DataFrame(mumbai100)
  mumbaidf.to_csv('mumbai.csv',index=False)  
  bangaloredf= pd.DataFrame(bangalore100)
  bangaloredf.to_csv('bangalore.csv',index=False)  
  punedf= pd.DataFrame(pune100)
  punedf.to_csv('pune.csv',index=False)   

  data=[mumbaidf,bangaloredf,punedf]
  zomatodf=pd.concat([mumbaidf,bangaloredf,punedf],axis=1,keys=['MUMBAI','BANGALORE','PUNE'])  
  zomatodf.to_csv('zomato100.csv',index=False) 

  

 
  
    


    
 
        
