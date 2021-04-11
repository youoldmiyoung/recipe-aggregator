
from bs4 import BeautifulSoup
import requests

'''The current problem is SOLVED [that the txt files are being overwritten every time I run the crawler so when I have scraped multiple blogs, I need to make sure somehow the txt files can be appended without duplicates]'''

from bs4 import BeautifulSoup
import requests

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
                with open('recipes/scrap.html', 'a') as f:
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
            with open('recipes/scrap.html', 'a') as f:
                f.write(f'''

    <h2>{hyperL}</h2>
    <{finalPic}>

                ''')
            # appList.append([titleActual, hyperL, finalPic])

#write the file
    # for elem in appList:
    #     with open('recipes/appetizers.txt', 'w') as f:
    #         f.write(f'appList = {appList}')

    # newPath = shutil.copy('recipes/appetizers.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/apps/apps.py')

    # print('just added something yummy to appetizers!')


OFDappetizers()