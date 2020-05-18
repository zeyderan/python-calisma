from bs4 import BeautifulSoup
import requests
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

list = soup.find('tbody',{"class":"lister-list"}).find_all('tr',limit=10)

for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find('a').text
    yil = tr.find("td",{"class":"titleColumn"}).find('span').text.strip('()')
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find('strong').text
    print(title, yil, rating)
