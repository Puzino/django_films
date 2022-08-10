import requests
from bs4 import BeautifulSoup


def handler():
    url = 'https://www.kinonews.ru/movies_waitings/'
    responce = requests.get(url)

    soup = BeautifulSoup(responce.text, 'html.parser')
    divbody = soup.find_all('div', class_="relative")

    links = []
    for i in divbody:
        try:
            a = i.find('a', class_='titlefilm').get('href')
            links.append(f'https://www.kinonews.ru{a}')
        except:
            pass

    for x in links[:1]:
        link_movie = requests.get(x)
        link_soup = BeautifulSoup(link_movie.text, 'html.parser')
        link_div = link_soup.find('div', class_='block-page-new')
        name_movie = link_div.find('h1', class_="film").text
        text_movie = link_div.find('div', class_="textart15").text
        print(text_movie)
        print(link_div)

handler()
