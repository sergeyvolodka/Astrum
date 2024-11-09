import telebot
from telebot.types import Message, ReplyKeyboardMarkup as RKM, InlineKeyboardMarkup as IKM, \
    InlineKeyboardButton as IKB, CallbackQuery as CQ, ReplyKeyboardRemove as RKR
from config import TOKEN
import asyncio

bot = telebot.TeleBot(TOKEN)
delite = RKR()

@bot.message_handler(commands=['start'])
def start(m: Message):
    kb = RKM(resize_keyboard=True)
    kb.row('🛒 Купить товар')
    bot.send_message(m.chat.id,
                     text='Astrum Shop:\n👋Привет! Приветствуем в магазине официального канала - @MAKWARE'
                          ' \nОтзывы - @astrumOt\n👨‍💻В данном боте ты можешь приобрести '
                          'премиум '
                          'чит для игры Standoff 2 без бана и Без рут прав. ',
                     reply_markup=kb)


@bot.message_handler(commands=["buy"])
def buy(m: Message):
    kb = IKM()
    kb.row(IKB(text="Astrum privat", callback_data="privat"))
    bot.send_message(m.chat.id,text='Ожидайте',reply_markup=delite)
    asyncio.run(asyncio.sleep(2))
    bot.send_message(m.chat.id, text="Жми кнопку, чтобы купить чит!⬇", reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback(call: CQ):
    if call.data == 'privat':
        kb = IKM()
        kb.row(IKB(text='Карта мир', callback_data="mir"))
        kb.row(IKB(text='ЮMoney', callback_data='youmoney'))
        bot.send_message(call.message.chat.id, text='PREMIUM ASTRUM CHEAT\nЦена: 30 дней - 150р, на всегда 200р\nЧит '
                                                    'полностью без БАНА и без ROOT прав.\n1️⃣ПО позволяет делать почти '
                                                    'все что можно -  летать,  убивать через стены, видеть игроков '
                                                    'через стены, выдавать дорогие скины, прыгать по карте и так далее\n'
                                                    '2️⃣С софтом вы можете играть в стиле LEGIT и RAGE.\n3️⃣ Почти каждый '
                                                    'день выходят обновления в приватной группе, добавляются функции и '
                                                    'всякие плюшки.'
                                                    '\n❗️Полный функционал чита вы можете увидеть - @MAKWARE\n❗️После оплаты'
                                                    ' вы получаете приватную  группу, в ней инструкции, сам чит, новости '
                                                    'о чите, чат.\n❗️Отзывы покупателей - @astrumOt',reply_markup=kb)

    if call.data == 'mir':
        bot.edit_message_reply_markup(call.message.chat.id,call.message.message_id)
        bot.send_message(call.message.chat.id, text='[f')

@bot.message_handler(content_types=['text'])
def text(m: Message):
    if m.text == '🛒 Купить товар':
        buy(m)


bot.infinity_polling()
