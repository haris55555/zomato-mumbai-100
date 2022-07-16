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

def parse_place():
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
def send_email(body):
   
  try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()   # optional
    
    S_email='harisjovian777@gmail.com'
    R_email='hai.advisoryservices@gmail.com'
    S_password=os.environ['gmail_password']
    
    subject='list of top 100 restaurant in Mumbai for zomato'
    
    emailtext="""\
    From:{S_email}
    To:{R_email}
    Subject:{subject}
    {body}
    """

    server.login(S_email,S_password)
    server_ssl.sendmail(S_email,R_email,emailtext)
    server_ssl.close()
  except:
    print ('Something went wrong...')
    
if __name__ =="__main__":
  driver = get_driver()
  places=get_places(driver)   
  print('fetching top 100 places')
  x = get_places(driver)
  print(len(x))
  places_data = parse_place()
  print(places_data)
  #saving file to_csv
  places_df= pd.DataFrame(places_data)
  print(places_data)  
  places_df.to_csv('MUMBAI100.csv',index=False) 

  print('send the result over email')
  body=json.dumps(places_data, indent=2)
  send_email(body)
  print('DONE')
    
  
    


    
 
        
