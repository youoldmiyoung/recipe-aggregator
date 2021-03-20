
from bs4 import BeautifulSoup
import requests

url = 'https://olivesfordinner.com/category/appetizers/page/2'
response = requests.get(url)
htmlText = response.text

soup = BeautifulSoup(htmlText, 'lxml')
links = soup.find_all('article')
for image in links[0:13]:
    x = image.find('img')
    final = x.attrs['src']
    print(final)
    break
