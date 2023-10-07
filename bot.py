import asyncio, time, logging

from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
from handlers import other_handlers, user_handlers, admins_handlers
from keyboards.main_menu import set_main_menu
from book_parsing.text_parsing import create_book_text
from services.file_handling import book, prepare_book


logger = logging.getLogger(__name__)
# BOOK_PATH = 'book/book.txt'

# конфигурация и запуск бота
async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    
    # информация о запуске
    logger.info('запустился')

    # конфиг
    config: Config = load_config()

    # бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # главное меню бота
    await set_main_menu(bot)

    # парсинг книги с сайта
    create_book_text()

    # # подготовка книги
    # prepare_book(BOOK_PATH)
    
    # роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(admins_handlers.router)
    dp.include_router(other_handlers.router)
    

    # удаляем апдейты и start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    
