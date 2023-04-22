from aiogram import Bot, Dispatcher,types
from aiogram.utils import executor
from translator import tarjimon


API_TOKEN = "YOU API TOKEN"
bot = Bot(token=API_TOKEN)
dp=Dispatcher(bot=bot)

@dp.message_handler(commands='start')
async  def welcome(message:types.Message):
    await message.answer(f'Assalom aleykum .\n Xush kelibsiz {message.from_user.full_name} ! \n Menga uzbek tilida matn yuboring . \n Men uni ingliz tiliga tarjima qilib beraman : ')

@dp.message_handler(content_types='text')
async def message_send(message:types.Message):
    text = message.text
    tarjima = tarjimon(text)
    await message.reply(tarjima)

if __name__=='__main__':
    executor.start_polling(dispatcher=dp)
