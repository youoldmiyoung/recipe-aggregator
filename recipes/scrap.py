
from bs4 import BeautifulSoup
import requests


breLinkList = []
breTitleList = []
breList3 = []
breFinalList = []
brePicList = []

def OFDbreakfast():
    print('OFD breakfast time, yum!')
    #get the link
    urlA = 'https://olivesfordinner.com/category/breakfast-and-brunch/page/{}'
    for i in range(2,5): 
        url = urlA.format(i)
        response = requests.get(url)
        htmlText = response.text
        #make the soup
        soup = BeautifulSoup(htmlText, 'lxml')
        #parse the soup
        links = soup.find_all('article')
        #there are 12 recipe titles per page, 
        #find the links and titles and put them each into a list
        for title in links[0:13]:
            titleActual = title.get('aria-label')
            if 'Giveaway' not in titleActual:
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in breTitleList:
                    breTitleList.append(titleActual)
                    breLinkList.append(hyperL)

        #scrape the image
        #BREAKFAST 1
        for image in links[0:13]: 
            x = image.find('img')
            finalPic = x.attrs['src']
            if 'giveaway' not in finalPic:
                if finalPic not in brePicList:
                    brePicList.append(finalPic)

    #different code for page 1 of each category due to diff link formatting on website
    url = 'https://olivesfordinner.com/category/breakfast-and-brunch'
    print('making soup...')
    response = requests.get(url)
    htmlText = response.text
    soup = BeautifulSoup(htmlText, 'lxml')
    links = soup.find_all('article')
    for title in links[0:13]:
        titleActual = title.get('aria-label')
        if 'Giveaway' not in titleActual:
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            if titleActual not in breTitleList:
                breTitleList.append(titleActual)
                breLinkList.append(hyperL)
    #scrape the image
    #BREAKFAST 2
        for image in links[0:13]: 
            x = image.find('img')
            finalPic = x.attrs['src']
            if 'giveaway' not in finalPic:
                if finalPic not in brePicList:
                    brePicList.append(finalPic)
    #pair titles and links together
    breList3.append([[x,y] for x,y in zip(breTitleList, breLinkList)])
    print('checking for duplicates...')

    #erase duplicates
    for item in breList3:
        if item not in breFinalList:
            breFinalList.append(item) 
    
    print(brePicList)

OFDbreakfast()
