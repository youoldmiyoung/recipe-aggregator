#pip install lxml

from bs4 import BeautifulSoup
import requests

#don't want the lists to be re-written every time we call the OFDapps function
appLinkList = []
appTitleList = []
appList3 = []
appfinalList = []

#get the link, make the soup, parse the soup, erase duplicates, write the file.
def OFDappetizers():
    print('OFD appetizer time, yum!')

    #get the link
    urlA = 'https://olivesfordinner.com/category/appetizers/page/{}'
    print('making soup...')

    for i in range(2,11): 
        url = urlA.format(i)
        
        response = requests.get(url)
        htmlText = response.text
        
        #make the soup
        soup = BeautifulSoup(htmlText, 'lxml')
        #parse the soup
        links = soup.find_all('article')

        #there are 12 recipe titles per page, 
        #find the links and titles and put them each into a list
        for title in links[0:12]:
            titleActual = title.get('aria-label')
            if 'Giveaway' not in titleActual:
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in appTitleList:
                    appTitleList.append(titleActual)
                    appLinkList.append(hyperL)

    #pair titles and links together
    appList3.append([[x,y] for x,y in zip(appTitleList, appLinkList)])

    print('checking for duplicates...')
    
    #erase duplicates
    for item in appList3:
        if item not in appfinalList:
            appfinalList.append(item) 

    #write the file
    for elem in appfinalList:
        with open('recipes/appetizers.txt', 'w') as f:
            f.write('\n \n'.join(map(str, appfinalList)))
            print('just added something yummy to appetizers!')

entLinkList = []
entTitleList = []
entList3 = []
entfinalList = []

def OFDentrees():
    print('OFD entree time, yum!')

    #get the link
    urlA = 'https://olivesfordinner.com/category/entrees/page/{}'
    print('making soup...')
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
        for title in links[0:12]:
            titleActual = title.get('aria-label')
            if 'Giveaway' not in titleActual:
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in entTitleList:
                    entTitleList.append(titleActual)
                    entLinkList.append(hyperL)

    #pair titles and links together
    entList3.append([[x,y] for x,y in zip(entTitleList, entLinkList)])

    print('checking for duplicates...')
    
    #erase duplicates
    for item in entList3:
        if item not in entfinalList:
            entfinalList.append(item) 

    #write the file
    for elem in entfinalList:
        with open('recipes/entrees.txt', 'w') as f:
            f.write('\n \n'.join(map(str, entfinalList)))
            print('just added something yummy to entrees!')


desLinkList = []
desTitleList = []
desList3 = []
desFinalList = []

def OFDdesserts():
    print('OFD dessert time, yum!')

    #get the link
    urlA = 'https://olivesfordinner.com/category/dessert/page/{}'
    print('making soup...')

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
        for title in links[0:12]:
            titleActual = title.get('aria-label')
            if 'Giveaway' not in titleActual:
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in desTitleList:
                    desTitleList.append(titleActual)
                    desLinkList.append(hyperL)

    #pair titles and links together
    desList3.append([[x,y] for x,y in zip(desTitleList, desLinkList)])

    print('checking for duplicates...')
    
    #erase duplicates
    for item in desList3:
        if item not in desFinalList:
            desFinalList.append(item) 

    #write the file
    for elem in desFinalList:
        with open('recipes/desserts.txt', 'w') as f:
            f.write('\n')
            f.write('\n \n'.join(map(str, desFinalList)))
            print('just added something yummy to desserts!')

OFDdesserts()
OFDappetizers()
OFDentrees()
