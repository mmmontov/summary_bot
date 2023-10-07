from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON

router = Router()

@router.message()
async def send_other_message(message: Message):
    await message.answer(text=LEXICON['unknown_command'])

