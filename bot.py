import logging
# import telebot
import random
# from aiogram import *
from aiogram import Bot, Dispatcher, executor, types
import configparser
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import CommandStart


# from telebot import types



config = configparser.ConfigParser()
config.read('config.ini')

API_TOKEN = config.items("BOT")[0][1]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




#varibles 
help1 = "Все команды бота: \n/start - Приветствие"


def auth(func):
	async def wrapper(message):
		if message["from"]["id"] == 925356318:
			return await func(message)
	return wrapper


@dp.message_handler(commands=['test'])
@auth
async def test(message: types.Message):
	await message.answer("PRIVET")


@dp.message_handler(commands=['message2'])
async def test(message: types.Message):
	t = message.chat.type
	if t == "private":
		await message.answer("PRIVET")
	elif t == "supergroup":
		await message.answer("Вы можете только"
							 " в лс исп. эту команду")





@dp.message_handler(lambda message: message.text.lower() == "привет")
async def messages(message: types.Message):
	await bot.send_message(message.chat.id, 'Как дела? Если ты Бочок напиши 1')
    
@dp.message_handler(lambda message: message.text.lower() == "1")
async def messages(message: types.Message):
	await bot.send_message(message.chat.id, 'Как дела? Если ты Бочок напиши 1')
    


		# bot.send_message(message.chat.id, 'Поздравляю ты Бочок')



# @dp.message_handler(commands=['test'])
# async def test(message: types.Message):
# 	rnd = random.choice(["0", "1", "2", "3"])
# 	if rnd == "0":
# 		print("0")
# 	if rnd == "2":
# 		print("2")
# 	if rnd == "3":
# 		print("3")
# 	else:
# 		print("
# 1")

# @dp.message_handler(lambda message: message.text.lower() == 'привет')
# async def process_command_1(message: types.Message):
# 	await message.answer("PRIVET")





	# await bot.send_message(message.chat.id, random.choice(["1", "2", "3"]))
	# await message.answer(message)




# @dp.message_handler(commands=['start'])  #отправка стикера при команде старт
# def welcome(message):
# 	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный что бы веселить всех.".format(message.from_user, bot.get_me()),parse_mode='html')
# 	bot.send_message(message.chat.id, help1)


# @dp.message_handler(commands=['help'])  #отправка стикера при команде старт
# def welcome222(message):
# 	bot.send_message(message.chat.id, help1)


# @dp.message_handler(content_types=['text'])
# def testmsg(message):
# 	if message.text == 'Привет':             #если написали ---- то
# 		bot.reply_to(message, 'Привет бро')   #ответить на сообщение
# 		bot.send_message(message.chat.id, 'Как дела?')
# 	elif message.text == 'привет':             #если написали ---- то
# 		bot.reply_to(message, 'Привет бро')   #ответить на сообщение
# 		bot.send_message(message.chat.id, 'Как дела?')
# 	elif message.text == 'Нормально':            
# 		bot.send_message(message.chat.id, 'Я рад что всё нормально')
# 	elif message.text == 'Не очень':             
# 		bot.send_message(message.chat.id, 'Бывает')
# 	elif message.text == 'Плохо':            
# 		bot.send_message(message.chat.id, 'Всё будет ОК')
# 	elif message.text == 'Норм':           
# 		bot.send_message(message.chat.id, 'Я рад что всё норм')
# 	elif message.text == 'Как дела?':             
# 		bot.send_message(message.chat.id, 'У меня всегда хорошие дела!:)')
# 	elif message.text == 'как дела?':            
# 		bot.send_message(message.chat.id, 'У меня всегда хорошие дела!:)')
# 	elif message.text == 'Yjhv':             
# 		bot.send_message(message.chat.id, 'Я рад что всё норм')
# 	elif message.text == 'yjhv':             
# 		bot.send_message(message.chat.id, 'Я рад что всё норм')
# 	elif message.text == 'норм':            
# 		bot.send_message(message.chat.id, 'Я рад что всё норм')
# 	elif message.text == 'не очень':          
# 		bot.send_message(message.chat.id, 'Бывает')
# 	elif message.text == 'Yt jxtym':             
# 		bot.send_message(message.chat.id, 'Бывает')
# 	elif message.text == 'yt jxtym':             
# 		bot.send_message(message.chat.id, 'Бывает')
# 	elif message.text == 'Gkj[j':             
# 		bot.send_message(message.chat.id, 'Всё будет ОК:)')
# 	elif message.text == 'gkj[j':            
# 		bot.send_message(message.chat.id, 'Всё будет ОК:)')
# 	elif message.text == 'плохо':           
# 		bot.send_message(message.chat.id, 'Всё будет ОК:)')
# 	elif message.text == 'Такое':             #если написали ---- то
# 		bot.send_message(message.chat.id, 'Всё будет ОК:)')
# 	elif message.text == 'Ага':             #если написали ---- то
# 		bot.send_message(message.chat.id, 'Ага... Конечно')




if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
