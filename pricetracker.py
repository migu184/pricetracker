#import time
#import requests #for sending request to amazon
#from bs4 import BeautifulSoup #for getting values from  response...
from urllib.request import Request, urlopen

req = Request(
    url='https://www.amazon.com.mx/Consola-Digital-Horizon-Forbidden-WestTM/dp/B0B5JCBX6M', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
print(webpage)