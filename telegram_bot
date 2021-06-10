import telebot

bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Ciao bello, appena so qualcosa te fo' sape'!!!")

def alarm():
    bot.send_message('chat_id',"MUOVITI VAI SUL CARRELLO CHE CE STA NA PS5 BELLA FRESCA!!!")        #chat_id non è una stringa

if __name__=="__main__":
    bot.polling()
