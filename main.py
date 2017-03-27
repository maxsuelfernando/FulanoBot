import telebot
import constants
import os

bot = telebot.TeleBot(constants.token)

# bot.send_message(216582785, "sucesso!")

# upd = bot.get_updates()

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

# print(bot.get_me())

@bot.message_handler(commands=["ajuda"])
def handle_text(message):
    bot.send_message(message.chat.id, "Bem vindo ao tópico de ajudas!")

@bot.message_handler(content_types=["new_chat_member"])
def send_welcome(message):
    nome = format(message.new_chat_member.first_name)
    bot.send_message(message.chat.id, "Oi, " + nome + ", Seja bem vindo!")

@bot.message_handler(content_types=["text"])
def handle_text(message):
   if message.text == "oi":
       bot.send_message(message.chat.id, "Olá, " + message.chat.first_name + " seja bem-vindo!")
   elif message.text == "Oi":
       bot.send_message(message.chat.id, "Olá, " + message.chat.first_name + " seja bem-vindo!")
   elif message.text == "OI":
       bot.send_message(message.chat.id, "Olá, " + message.chat.first_name + " seja bem-vindo!")

bot.polling(none_stop=True, interval=0)