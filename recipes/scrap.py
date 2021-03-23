
from bs4 import BeautifulSoup
import requests

'''The current problem is that the txt files are being overwritten every time I run the crawler so when I have scraped multiple blogs, I need to make sure somehow the txt files can be appended without duplicates.'''

from bs4 import BeautifulSoup
import requests

def PULbreakfast():
    linkPrefix = 'https://www.pickuplimes.com/'
    breList = []
    print('PUL breakfast time, yum!')
    #get the link, type 7 is breakfast
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=7&page={}'
    for i in range(1,5): 
        url = urlA.format(i)
        
        response = requests.get(url)
        htmlText = response.text
        
        #make the soup
        soup = BeautifulSoup(htmlText, 'lxml')
        wrapper = soup.find('ul', class_='flex-container')
        item = wrapper.find_all('li', class_='flex-item slide-up-ani')

        for x in item:
            title = x.h3.text
            link = x.a['href']
            image = x.a.img.attrs['src']
            breList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])
