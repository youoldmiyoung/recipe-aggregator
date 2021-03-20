#pip install lxml
#(in order) appetizers, entrees, dessert, breakfast 

from bs4 import BeautifulSoup
import requests

#don't want the lists to be re-written every time we call the function
appLinkList = []
appTitleList = []
appList3 = []
appFinalList = []
appPicList = []
appList = []

#get the link, make the soup, parse the soup, erase duplicates, write the file.
def OFDappetizers():
    print('OFD appetizer time, yum!')
    #get the link
    urlA = 'https://olivesfordinner.com/category/appetizers/page/{}'

    for i in range(2,11): 
        url = urlA.format(i)
        
        response = requests.get(url)
        htmlText = response.text
        
        #make the soup
        soup = BeautifulSoup(htmlText, 'lxml')
        #parse the soup
        links = soup.find_all('article')

        #there are 12 recipe titles per page, 
        #find each title, link, pic and put them into a list
        for title in links[0:13]:
            titleActual = title.get('aria-label')
            if 'Giveaway' not in titleActual:
                finalPic = title.img.attrs['src']
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                appList.append([titleActual, hyperL, finalPic])


    #different code for page 1 of each category due to diff link formatting on website
    url = 'https://olivesfordinner.com/category/appetizers'
    print('making soup...')
    response = requests.get(url)
    htmlText = response.text
    soup = BeautifulSoup(htmlText, 'lxml')
    links = soup.find_all('article')

    for title in links[0:13]:
        titleActual = title.get('aria-label')
        if 'Giveaway' not in titleActual:
            finalPic = title.img.attrs['src']
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            appList.append([titleActual, hyperL, finalPic])

    #write the file
    for elem in appList:
        with open('recipes/appetizers.txt', 'w') as f:
            f.write('\n \n'.join(map(str, appList)))
    print('just added something yummy to appetizers!')

entLinkList = []
entTitleList = []
entList3 = []
entFinalList = []
entPicList = []
entList = []

def OFDentrees():
    print('OFD entree time, yum!')
    #get the link
    urlA = 'https://olivesfordinner.com/category/entrees/page/{}'
    for i in range(2,20): 
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
                finalPic = title.img.attrs['src']
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                entList.append([titleActual, hyperL, finalPic])

    #different code for page 1 of each category due to diff link formatting on website
    url = 'https://olivesfordinner.com/category/entrees/'
    print('making soup...')
    response = requests.get(url)
    htmlText = response.text
    soup = BeautifulSoup(htmlText, 'lxml')
    links = soup.find_all('article')

    for title in links[0:13]:
        titleActual = title.get('aria-label')
        if 'Giveaway' not in titleActual:
            finalPic = title.img.attrs['src']
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            entList.append([titleActual, hyperL, finalPic])

    #write the file
    for elem in entList:
        with open('recipes/entrees.txt', 'w') as f:
            f.write('\n \n'.join(map(str, entList)))
    print('just added something yummy to entrees!')

desLinkList = []
desTitleList = []
desList3 = []
desFinalList = []
desPicList = []
desList = []

def OFDdesserts():
    print('OFD dessert time, yum!')
    #get the link
    urlA = 'https://olivesfordinner.com/category/dessert/page/{}'
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
                finalPic = title.img.attrs['src']
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                desList.append([titleActual, hyperL, finalPic])

    #different code for page 1 of each category due to diff link formatting on website
    url = 'https://olivesfordinner.com/category/dessert/'
    print('making soup...')
    response = requests.get(url)
    htmlText = response.text
    soup = BeautifulSoup(htmlText, 'lxml')
    links = soup.find_all('article')

    for title in links[0:13]:
        titleActual = title.get('aria-label')
        if 'Giveaway' not in titleActual:
            finalPic = title.img.attrs['src']
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            desList.append([titleActual, hyperL, finalPic])

    #write the file
    for elem in desList:
        with open('recipes/desserts.txt', 'w') as f:
            f.write('\n \n'.join(map(str, desList)))
    print('just added something yummy to desserts!')


breLinkList = []
breTitleList = []
breList3 = []
breFinalList = []
brePicList = []
breList = []

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
                finalPic = title.img.attrs['src']
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                breList.append([titleActual, hyperL, finalPic])
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
            finalPic = title.img.attrs['src']
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            breList.append([titleActual, hyperL, finalPic])

    #write the file
    for elem in breList:
        with open('recipes/breakfast.txt', 'w') as f:
            f.write('\n \n'.join(map(str, breList)))
    print('just added something yummy to breakfast!')


OFDbreakfast()