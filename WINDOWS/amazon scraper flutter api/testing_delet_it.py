

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
}
response = requests.get('https://www.amazon.com/s?k=rtx',headers=headers)
print(response.text)
# soup = BeautifulSoup(response)
# response[200]

# amazon_link1 = "https://www.amazon.com/s?k=rtx"


# result = requests.get(amazon_link1)
# print(result.text)
from zenrows import ZenRowsClient 
 
client = ZenRowsClient(API_KEY) 
url = "https://www.amazon.com/Crockpot-Electric-Portable-20-Ounce-Licorice/dp/B09BDGFSWS" 
# It's possible to specify javascript rendering, premium proxies and geolocation. 
# You can check the API documentation for further customization. 
params = {"premium_proxy":"true","proxy_country":"us","autoparse":"true"} 
 
response = client.get(url, params=params) 
 
print(response.json())
  