from aiogram import Router
from aiogram.types import Message
from config_data.config import load_config
from lexicon.lexicon import LEXICON
from database.database import users_db, user_dict_template
from book_parsing.text_parsing import create_book_text
from services.file_handling import prepare_book, book
from time import sleep
from copy import deepcopy

config = load_config()

router = Router()

@router.message(lambda x: x.from_user.id in config.tg_bot.admin_ids)
async def process_change_book_url(message: Message):
    # print(config.tg_bot.admin_ids)
    if 'https' in message.text:
        new_url = message.text
        with open('book/book_url.txt', 'w', encoding='utf-8') as file:
            file.write(new_url)
        create_book_text()
        sleep(2)
        BOOK_PATH='book/book.txt'
        prepare_book(BOOK_PATH)
        # print('\n\nadmin\n\n', book[1])

        for user in users_db:
            users_db[user] = deepcopy(user_dict_template)
        await message.answer(text=LEXICON['book_url_changed'])
    else:
        await message.answer(text=LEXICON['unknown_url'])
    
