import requests
from bs4 import BeautifulSoup as BS
import re
import time
url = 'https://alcofan.com/category/marki-piva'

def beer_cards(url):
    for i in range(1,15):
        resp = requests.get(f'{url}/page/{i}')
        soup = BS(resp.text,'lxml')
        yield soup.find_all('div',{"id" : re.compile('^postid-\d+$')})

def Beer_Names_Gen(url):
    for cards in beer_cards(url):
        for card in cards:
            yield card.a.text
# s1 = time.time()
search_list = [name for name in Beer_Names_Gen(url)]
# s2 = time.time() - s1
def main():
    print(search_list)

if __name__ == '__main__':
    main()
# print(s2)