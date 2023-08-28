import asyncio
import telebot
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv 
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


#### Button Panel
main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('🇲🇩 Crypto Moldova').add('🏧 Crypto Exchange').add('📮 Contactează-ne')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('🇲🇩 Crypto Moldova').add('🏧 Crypto Exchange').add('📮 Contactează-ne').add('Admin Panel')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('🇲🇩 Crypto Moldova').add('🏧 Crypto Exchange').add('📮 Contactează-ne').add('Mass Messaging')

catalog_list1 = InlineKeyboardMarkup(row_width=2)
catalog_list1.add(InlineKeyboardButton(text='📰 Crypto Noutăți', url='https://t.me/MoldovaBitcoin'),
                 InlineKeyboardButton(text='💬 Crypto Chat', url='https://t.me/Crypto_Moldova'),
                 InlineKeyboardButton(text='📛 Crypto Scam', url='https://t.me/Crypto_Info_MD/3'),
                 InlineKeyboardButton(text='👨‍💻 Crypto Canale', url='https://t.me/Crypto_Info_MD/4'),
                 InlineKeyboardButton(text='✅ Crypto Pețitie', url='https://coinbank.md'))

catalog_list2 = InlineKeyboardMarkup(row_width=2)
catalog_list2.add(InlineKeyboardButton(text='🏧 Crypto ATM', url='https://t.me/MoldovaBitcoin'),
                 InlineKeyboardButton(text='🧾 Alte Alternative', url='https://t.me/Crypto_Info_MD/61'))



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_photo('https://us.123rf.com/450wm/promesaartstudio/promesaartstudio1712/promesaartstudio171200190/91040135-physical-version-of-bitcoin-litecoin-gold-us-dollar-and-moldova-flag-conceptual-image-for.jpg?ver=6')
    await message.answer(f'Salut {message.from_user.first_name}! Acest Crypto Bot te va ajuta să găsești un răspuns la orice întrebare referitoare la domeniul Crypto din Moldova 🇲🇩',
                         reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'V-ați autorizat ca Admin!', reply_markup=main_admin)

    
@dp.message_handler(commands=['id'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.id}')

    

#### Buttons

@dp.message_handler(text='🇲🇩 Crypto Moldova')
async def contacts(message: types.Message):
    await message.answer_photo('https://us.123rf.com/450wm/markoaliaksandr/markoaliaksandr1905/markoaliaksandr190502410/122092318-crypto-currency-gold-coin-bitcoin-btc-coin-bitcoin-against-the-background-of-the-flag-of-moldova.jpg?ver=6')
    await message.answer(f'🪙 Tot ce ține de Crypto în Moldova - găsești aici:', reply_markup=catalog_list1)

@dp.message_handler(text='🏧 Crypto Exchange')
async def contacts(message: types.Message):
    await message.answer_photo('https://thumbs.dreamstime.com/b/moldavian-lei-crypto-currency-concept-coins-221909201.jpg')
    await message.answer(f'🏦 Modalitățile de schimb Crypto/MDL - găsești aici:', reply_markup=catalog_list2)

@dp.message_handler(text='📮 Contactează-ne')
async def contacts(message: types.Message):
    await message.answer_photo('https://www.freshlime.com/wp-content/uploads/2022/10/text-messaging.jpg')
    await message.answer(f'✍️ Pentru oferte și întrebări. Ne poți scrie un mesaj privat aici! Poți expedia failuri, foto, video sau audio. Îți vom răspunde în cel mai scurt timp posibil.')

@dp.message_handler(text='Admin Panel')
async def contacts(message: types.Message):
     if message.from_user.id == int(os.getenv('ADMIN_ID')):
         await message.answer(f'Ați intrat în Panelul pentru Admini', reply_markup=admin_panel)
     else:
         await message.reply('Nu v-am înțeles....') 

#### Sent Sticker with Welcome Message 
@dp.message_handler(content_types=['https://coinbank.md/wp-content/uploads/2021/12/sintra-302.png'])
async def check_sticker(message: types.Message):
    await message.answer(message.photo.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)

#### Sent Docs/Photos with Welcome Message 
@dp.message_handler(content_types=['document', 'photo', 'video', 'text', 'video_note', 'group', 'voice', 'file'])
async def forward_message(message: types.Message):
     await bot.forward_message(os.getenv('GROUP_ID'), message.chat.id, message.message_id,)
     await message.reply("Îți mulțumim! Mesajul tău a fost trimis. Îţi vom răspunde cât mai curând posibil.")
async def reply_message(message: types.Message):
    await message.reply("This is a reply message!") 



@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Nu v-am înțeles....') 

  

if __name__ == '__main__':
    executor.start_polling(dp)      