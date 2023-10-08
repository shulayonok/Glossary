"""
# Словари

dictionary = {1: "Tomas", 2: "Helen", "3": True}

List = ((1, "tomas"), (2, "helen"), (3, True))
d = dict(List)
print(d)

dictionary[False] = "qwerty"

def search(key):
    if key in dictionary:
        return dictionary[key]

print(search(1))
print(dictionary)


with open("glossary.txt", "a", encoding="utf8") as file:
    file.write("Код от кабинета в пентагоне: 4321\n")

with open("glossary.txt", "r", encoding="utf8") as file:
    a = file.readlines()
    print(a)
"""

import telebot
import glossary

bot = telebot.TeleBot("5164933170:AAFLvh8zhdoCuk5FxmrG1o8C9AvyqaslMtU")
glossary.read()


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Доброго времени суток! Это глоссарий. Пожалуйста, введите определение.")


@bot.message_handler(content_types=["text"])
def search(message):
    bot.send_message(message.from_user.id, glossary.search(message.text.lower()))


bot.polling()
