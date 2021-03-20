
from bs4 import BeautifulSoup
import requests


entLinkList = []
entTitleList = []
entList3 = []
entFinalList = []
entPicList = []

url = 'https://olivesfordinner.com/category/entrees/'
print('making soup...')
response = requests.get(url)
htmlText = response.text
soup = BeautifulSoup(htmlText, 'lxml')
links = soup.find_all('article')
for title in links[0:13]:
    titleActual = title.get('aria-label')
    if 'Giveaway' not in titleActual:
        hyperL = title.find('header', class_ = 'entry-header').a['href']
        if titleActual not in entTitleList:
            entTitleList.append(titleActual)
            entLinkList.append(hyperL)

    #scrape the image
    #ENTREE 2
for image in links[0:13]: 
    x = image.find('img')
    finalPic = x.attrs['src']
    if 'giveaway' not in finalPic:
        if finalPic not in entPicList:
            entPicList.append(finalPic)

#pair titles and links together
entList3.append([[x,y,z] for x,y,z in zip(entTitleList, entLinkList, entPicList)])

print('checking for duplicates...')

#erase duplicates
for item in entList3:
    if item not in entFinalList:
        entFinalList.append(item) 

print(entList3)