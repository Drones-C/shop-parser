import requests as r

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

URL = "https://aliexpress.ru/wholesale?catId=0&initiative_id=SB_20201113104400&SearchText=drones"

response = r.get(URL).text
soup = BeautifulSoup(response, 'html.parser')
print(soup.prettify())