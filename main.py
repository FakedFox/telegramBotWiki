from config import *
from parser import dellTxt, img


# /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
		bot.reply_to(message, "\nНапиши (/help) что бы узнать то я могу\n Отвечаю на запросы Википедии! (/wiki)")

#  /help
@bot.message_handler(commands=["help"])
def send_welcome(message):
	bot.reply_to(message, "Отвечаю на запросы Википедии! (/wiki)\n")

# wiki seach
@bot.message_handler(commands=["wiki"])
def wiki_start(message):
	bot.reply_to(message, "Напишите запрос Википедии!")

	# wiki result
	@bot.message_handler(content_types=["text"])
	def wiki(message):
		bot.send_message(message.chat.id, '...')
		infoList = dellTxt(message.text)
		bot.send_photo(message.chat.id, photo=open(img(message.text), 'rb'))
		with open(infoList[3], 'r', encoding='utf-8') as f:
			bot.send_document(message.chat.id, f)
			f.seek(0)
			for i in range(infoList[1]):
				send = f.readline()
				bot.send_message(message.chat.id, send)



# BOT start
bot.polling(none_stop=True, interval=0)
