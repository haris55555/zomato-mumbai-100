import requests
from bs4 import BeautifulSoup
zomato_mumbai_url = "https://www.zomato.com/mumbai/great-food-no-bull"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}
response= requests.get(zomato_mumbai_url,headers=headers)

print('status code',response.status_code)
print('output',response.text[:1000])
with open ('top.html','w') as f:
  f.write(response.text)
  doc= BeautifulSoup(response.text,'html.parser')
  print('page title',doc.title.text)