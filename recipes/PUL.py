from bs4 import BeautifulSoup
import requests
from datetime import datetime
import shutil

stamp = datetime.now()

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

    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=8&page={}'
    for i in range(1,3): 
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

    for elem in breList:
        with open('recipes/breakfast.txt', 'w') as f:
            f.write(f'breList = {breList}')

    newPath = shutil.copy('recipes/breakfast.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/breakfast/breakfast.py')

    print('just added something yummy to breakfast!')

def PULappetizers():
    linkPrefix = 'https://www.pickuplimes.com/'
    appList = []
    print('PUL appetizer time, yum!')
    #get the link, type 3 is appetizers
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=3&page={}'
    for i in range(1,4): 
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
            appList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])
    for elem in appList:
        with open('recipes/appetizers.txt', 'w') as f:
            f.write(f'appList = {appList}')

    newPath = shutil.copy('recipes/appetizers.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/apps/apps.py')

    print('just added something yummy to appetizers!')



#snacks t10 and sauces t13, homemade staple (sauces) type 6
def PULsnacksnsauce():
    linkPrefix = 'https://www.pickuplimes.com/'
    snaList = []
    print('PUL snacks n sauce time, yum!')
    #get the link, type 6 is homemade staples
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=6&page={}'
    for i in range(1,3): 
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
            snaList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])
    #get the link, type 10 is snacks
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=10&page={}'
    for i in range(1,7): 
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
            snaList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])

    #get the link, type 13 is sauce
    url = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=13&page=1'
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
        snaList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])

    for elem in snaList:
        with open('recipes/snacksnsauce.txt', 'w') as f:
            f.write(f'snaList = {snaList}')

    newPath = shutil.copy('recipes/snacksnsauce.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/snacks/snacks.py')
    print('just added something yummy to snacks')

# soups t11, salads type 12, sides t4

def PULsoupsaladside():
    linkPrefix = 'https://www.pickuplimes.com/'
    souList = []
    print('PUL soup, salad, side time, yum!')
    #get the link, type 4 is sides
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=4&page={}'
    for i in range(1,3): 
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
            souList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])
    #get the link, type 11 is soup
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=11&page={}'
    for i in range(1,3): 
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
            souList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])

    #get the link, type 12 is salad
    url = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=12&page=1'
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
        souList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])

    for elem in souList:
        with open('recipes/soupsaladside.txt', 'w') as f:
            f.write(f'souList = {souList}')

    newPath = shutil.copy('recipes/soupsaladside.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/sides/sides.py')
    print('just added something yummy to soup, salad, side!')

#entree type 2
def PULentree():
    linkPrefix = 'https://www.pickuplimes.com/'
    entList = []
    print('PUL entree time, yum!')
    #get the link, type 2 is entrees
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=2&page={}'
    for i in range(1,8): 
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
            entList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])
    for elem in entList:
        with open('recipes/entrees.txt', 'w') as f:
            f.write(f'entList = {entList}')

    newPath = shutil.copy('recipes/entrees.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/entrees/entrees.py')

    print('just added something yummy to entrees!')



#drink type 9
def PULdrinks():
    linkPrefix = 'https://www.pickuplimes.com/'
    driList = []
    print('PUL drinks time, yum!')
    #get the link, type 9 is drinks
    urlA = 'https://www.pickuplimes.com/recipe/?sb=&meal_type=9&page={}'
    for i in range(1,3): 
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
            driList.append([f'{title}, https://www.pickuplimes.com{link}, {image}'])
    for elem in driList:
        with open('recipes/drinks.txt', 'w') as f:
            f.write(f'driList = {driList}')

    newPath = shutil.copy('recipes/drinks.txt', f'/Users/miagayle/Desktop/recipeWeb/recipes/drinks/drinks.py')
    print('just added something yummy to drinks!')


def runAllPUL():
    PULdrinks()
    PULappetizers()
    PULbreakfast()
    PULentree()
    PULsnacksnsauce()
    PULsoupsaladside()

runAllPUL()
