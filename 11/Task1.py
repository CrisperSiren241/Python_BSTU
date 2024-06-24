import requests
from bs4 import BeautifulSoup


def get_page_contents(url):

    page = requests.get(url)

    if page.status_code == 200:
        return page.text

    return None
    
def get_quotes_and_authors(page_contents):
    soup = BeautifulSoup(page_contents, 'lxml')
    quotes = soup.find_all('span', class_='text')
    return quotes
        
if __name__ == '__main__':
    url = 'http://quotes.toscrape.com'
    page_contents = get_page_contents(url)

    quotes= get_quotes_and_authors(page_contents)
    for i in range(len(quotes)):
        print(quotes[i].text)
        print()



