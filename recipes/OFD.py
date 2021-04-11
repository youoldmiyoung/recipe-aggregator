#pip install lxml
#(in order) appetizers, entrees, dessert, breakfast 

from bs4 import BeautifulSoup
import requests
from datetime import datetime
import shutil


#get the link, make the soup, parse the soup, erase duplicates, write the file.
def headerHTML():
    with open('recipes/scrap.html', 'w') as f:
        f.write('''
        {% extends 'base.html' %}

{% block content %}

<h1>appetizers</h1> 
<ul> 
        ''')

def OFDappetizers():
    headerHTML()

    appList = []
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
                finalPic = '<img src="' + title.img.attrs['src'] + '">'
                hyperL = '<a href="' + title.find('header', class_ = 'entry-header').a['href'] + f'">{titleActual}</a>'
                appList.append([finalPic, hyperL])
                with open('recipes/apps.html', 'a') as f:
                    f.write(f'''

    <h2>{hyperL}</h2>
    <{finalPic}>

                ''')
                # appList.append([titleActual, hyperL, finalPic])


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
            finalPic = '<img src="' + title.img.attrs['src'] + '">'
            hyperL = '<a href="' + title.find('header', class_ = 'entry-header').a['href'] + f'">{titleActual}</a>'
            #appList.append([finalPic, hyperL])
            #to write
            with open('recipes/apps.html', 'a') as f:
                f.write(f'''

    <h2>{hyperL}</h2>
    <{finalPic}>

                ''')
    with open ('recipes/apps.html', 'a') as f:
        f.write('</ul>')

def OFDentrees():
    entList = []
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
            f.write(f'entList = {entList}')

    newPath = shutil.copy('recipes/entrees.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/entrees/entrees.py')

    print('just added something yummy to entrees!')

def OFDdesserts():
    desList = []
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
            f.write(f'desList = {desList}')

    newPath = shutil.copy('recipes/desserts.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/desserts/desserts.py')
    print('just added something yummy to desserts!')

        


def OFDbreakfast():
    breList = []
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
            f.write(f'breList = {breList}')

    newPath = shutil.copy('recipes/breakfast.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/breakfast/breakfast.py')
    print('just added something yummy to breakfast!')

def runAll():
    OFDappetizers()
    OFDentrees()
    OFDdesserts()
    OFDbreakfast()

runAll()
