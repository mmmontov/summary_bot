import os, sys, re

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 800

book: dict[int, str] = {}

# возвращает строку с текстом и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    symbols = [',', '.', '!', ':', ';', '?']
    page_end = start+size
    page = text[start:page_end]
    while page[-1] not in symbols or len(text) > page_end+1 and text[page_end] in symbols: 
        page_end -= 1
        page = text[start:page_end]
    return (page, len(page))
    


# формирует словарь из кнниги
def prepare_book(path: str):

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    if re.search(r'Глава \d', text) is None:
        counter = 1
        while text:
            page, size = _get_part_text(text, 0, PAGE_SIZE)
            book[counter] = page.strip()
            text = text.replace(page, '')
            counter += 1 
        
    else:
        chapters = text.split('Глава')[1:]
        counter = 1
        for chapter in chapters:
            book[counter] = 'Глава ' + chapter.strip()
            counter += 1


    for i in range(counter, len(book)+1):
        del book[i]

    # print('\n\nchanged book\n\n', book)

# подготовка книги

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))