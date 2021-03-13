#pip install lxml

from bs4 import BeautifulSoup
import requests

url = 'https://olivesfordinner.com/category/appetizers/page/2'
response = requests.get(url)
htmlText = response.text



soup = BeautifulSoup(htmlText, 'lxml')
links = soup.find_all('article')

linkList = []
titleList = []

#there are 12 recipe titles per appetizer page, 
#find the links and titles and put them each into a list
for link in links[0:12]:
    hyperL = link.find('header', class_ = 'entry-header').a['href']
    linkList.append(hyperL)
for title in links:
        x = title.get('aria-label')
        titleList.append(x)

#pair the title with its corresponding link in a new list
list3 = [[x,y] for x,y in zip(titleList, linkList)]

zzz = list3[8][1]
print(zzz)

#to write list3 into the text file.
'''for elem in list3:
    with open('test.txt', 'w') as f:
        f.write('\n \n'.join(map(str, list3)))'''





# lis = []
# for link in links:
#     title = link.get('title')
#     if title == None:
#         continue
#     lis.append(title)


# print('done!')
