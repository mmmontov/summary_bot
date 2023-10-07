import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



def create_book_text():
    headers = {'user-agent':UserAgent().random}
    with open('book/book_url.txt', 'r', encoding='utf-8') as file:
        url = file.read()

    responce = requests.get(url=url, headers=headers)
    responce.encoding = 'utf-8'

    soup = BeautifulSoup(responce.text, 'lxml')
    start = soup.find('h2', id='sub5')
    if start.text != 'Краткое содержание':
        start = soup.find('h2', id='sub4')
    end = soup.find('div', class_='kratkoe-itogi')

    text_start = responce.text.find(str(start))
    text_end = responce.text.find(str(end))
    # print(start.text)
    # print(text_start)
    # print(text_end)

    text = responce.text[text_start:text_end]
    

    soup = BeautifulSoup(text, 'lxml')
    ads = len(soup.find_all('div', class_='ads-block'))

    for _ in range(ads):
        ad = soup.find('div', class_='ads-block')
        ad.decompose()

    summary_text = soup.text

    with open('book/book.txt', 'w', encoding='utf-8') as file:
        file.write(summary_text.strip())


if __name__ == '__main__':
    create_book_text()