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
        #find the links and titles and put them each into a list
        for title in links[0:13]:
            titleActual = title.get('aria-label')
            if 'Giveaway' not in titleActual:
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in appTitleList:
                    appTitleList.append(titleActual)
                    appLinkList.append(hyperL)
        #scrape the image
        #APP1
        for image in links[0:13]: 
            x = image.find('img')
            finalPic = x.attrs['src']
            if 'giveaway' not in finalPic:
                if finalPic not in appPicList:
                    appPicList.append(finalPic)


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
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            if titleActual not in appTitleList:
                appTitleList.append(titleActual)
                appLinkList.append(hyperL)
    #scrape the image
    #APP2
    for image in links[0:13]: 
            x = image.find('img')
            finalPic = x.attrs['src']
            if 'giveaway' not in finalPic:
                if finalPic not in appPicList:
                    appPicList.append(finalPic)
    #pair titles and links together, from both the multi-page scrape and single first page scrape
    appList3.append([[x,y,z] for x,y,z in zip(appTitleList, appLinkList, appPicList)])

    print('checking for duplicates...')
    
    #erase duplicates
    for item in appList3:
        if item not in appFinalList:
            appFinalList.append(item) 

    #write the file
    for elem in appFinalList:
        with open('recipes/appetizers.txt', 'w') as f:
            f.write('\n \n'.join(map(str, appFinalList)))
            print('just added something yummy to appetizers!')

entLinkList = []
entTitleList = []
entList3 = []
entFinalList = []
entPicList = []

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
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in entTitleList:
                    entTitleList.append(titleActual)
                    entLinkList.append(hyperL)
        
        #scrape the image
        #ENTREE 1
        for image in links[0:13]: 
            x = image.find('img')
            finalPic = x.attrs['src']
            if 'giveaway' not in finalPic:
                if finalPic not in entPicList:
                    entPicList.append(finalPic)

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

    #write the file
    for elem in entFinalList:
        with open('recipes/entrees.txt', 'w') as f:
            f.write('\n \n'.join(map(str, entFinalList)))
            print('just added something yummy to entrees!')


desLinkList = []
desTitleList = []
desList3 = []
desFinalList = []
desPicList = []

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
                hyperL = title.find('header', class_ = 'entry-header').a['href']
                if titleActual not in desTitleList:
                    desTitleList.append(titleActual)
                    desLinkList.append(hyperL)
        #scrape the image
        #DESSERT 1
        for image in links[0:13]: 
            x = image.find('img')
            finalPic = x.attrs['src']
            if 'giveaway' not in finalPic:
                if finalPic not in desPicList:
                    desPicList.append(finalPic)
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
            hyperL = title.find('header', class_ = 'entry-header').a['href']
            if titleActual not in desTitleList:
                desTitleList.append(titleActual)
                desLinkList.append(hyperL)
    #scrape the image
    #DESSERT 2
    for image in links[0:13]: 
        x = image.find('img')
        finalPic = x.attrs['src']
        if 'giveaway' not in finalPic:
            if finalPic not in desPicList:
                desPicList.append(finalPic)

    #pair titles and links together
    desList3.append([[x,y,z] for x,y,z in zip(desTitleList, desLinkList, desPicList)])
    print('checking for duplicates...')

    #erase duplicates
    for item in desList3:
        if item not in desFinalList:
            desFinalList.append(item) 

    #write the file
    for elem in desFinalList:
        with open('recipes/desserts.txt', 'w') as f:
            f.write('\n \n'.join(map(str, desFinalList)))
            print('just added something yummy to desserts!')

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
    breList3.append([[x,y,z] for x,y,z in zip(breTitleList, breLinkList, brePicList)])
    print('checking for duplicates...')

    #erase duplicates
    for item in breList3:
        if item not in breFinalList:
            breFinalList.append(item) 

    #write the file
    for elem in breFinalList:
        with open('recipes/breakfast.txt', 'w') as f:
            f.write('\n \n'.join(map(str, breFinalList)))
            print('just added something yummy to breakfast!')

print(brePicList)