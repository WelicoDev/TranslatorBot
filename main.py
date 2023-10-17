import logging
from aiogram import Bot, Dispatcher, executor, types
from oxfordLookup import getDefinitions
from googletrans import Translator

translator = Translator()

API_TOKEN = '6342905095:AAGHgfZ-r7_Aw9rtSyTGLBY8gjxqCsAtpI8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply("Assalom aleykum !\nMen TranslatorBot !\nSizga tarjima qilishda yordam beraman")
    await message.reply("Tarjima qilmoqchi bo'lgan so'zni yoki gapni  kiriting :>> 👉 ")
    
@dp.message_handler(commands='help')
async def send_help(message: types.Message):
    await message.reply("Sizga nima yordam kerak ? :>> ")
    await message.answer("Men nima vazifalarni bajara olaman ? \n1. ingliz tilida so'zlarni mano 'sini qaytarish (audio ham) \n2. ingliz tilidagi gaplarni uzbek tiliga tarjima qilish \n3. uzbek tilidagi gaplarni ingliz tiliga tarjima qilish !")
    await message.answer("Botdagi kamchiliklar yoki takliflar uchun murojaat qiling @welicodev 👨🏻‍💻")
    await message.answer("Kamchiliklar uchun uzr so'raymiz!")
    

@dp.message_handler()
async def send_translator(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text , dest).text)
        
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text , dest='en').text
            
        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions: \n{lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply('Bunday so\'z topilmadi 🥺')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)