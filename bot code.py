from email import message
import json
import requests
import telebot
from requests import delete
from telebot import types
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot('5745290423:AAGOtaErmk1Krm2e4Y1HlF9bj8IdsaBm0hs')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
stop_b = types.KeyboardButton('/Stop')
markup.add(stop_b)


# telebot.apihelper.proxy = {'http': 'socks5h://telegram.vpn99.net:55655'}
@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stop_b = types.KeyboardButton('/Stop')
    markup.add(stop_b)
    bot.send_message(message.chat.id, 'Enter your group', reply_markup=markup)


@bot.message_handler(commands=['Stop'])
def button_message(message):
    bot.send_message(message.chat.id, 'Put "/start" to return, see you! <3', reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types='text')
def send_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stop_b = types.KeyboardButton('/Stop')
    markup.add(stop_b)

    a = message.text
    a = a.upper()
    bot.send_message(message.chat.id, "Рассписание группы " + a + " на эту неделю:")
    s = "https://ruz.hse.ru/api/search?term=" + a + "&type=group"
    solditems_for_id = requests.get(s)  # (your url)
    data_id = solditems_for_id.json()
    for i_id in data_id:
        if i_id["label"] == a:
            id_dd = i_id["id"]

    s2 = "https://ruz.hse.ru/api/schedule/group/" + id_dd + "?start=2022.10.17&finish=2022.10.23&lng=1"
    solditems = requests.get(s2)  # (your url)
    data = solditems.json()
    s_mes = ""
    s_dat = ["", "", "", "", "", ""]
    k = [0, 0, 0, 0, 0, 0]
    for i in data:
        if i["dayOfWeekString"] == "Пн":
            k[0] += 1
        if i["dayOfWeekString"] == "Вт":
            k[1] += 1
        if i["dayOfWeekString"] == "Ср":
            k[2] += 1
        if i["dayOfWeekString"] == "Чт":
            k[3] += 1
        if i["dayOfWeekString"] == "Пт":
            k[4] += 1
        if i["dayOfWeekString"] == "Сб":
            k[5] += 1

    # for j in range(0,6):
    #     bot.send_message(message.chat.id,k[j])

    for j in range(0, 6):
        for i in data:
            # Monday
            if (k[j] > 0):
                if i["dayOfWeekString"] == "Пн":
                    if j == 0:
                        s_dat[0] += i["contentTableOfLessonsName"] + ")" + i["beginLesson"] + " " + i[
                            "dayOfWeekString"] + "  " + i["kindOfWork"] + "      " + i["discipline"] + "\n"
                        k[j] -= 1

            # Thusday
            if (k[j] > 0):
                if i["dayOfWeekString"] == "Вт":
                    if j == 1:
                        s_dat[1] += i["contentTableOfLessonsName"] + ")" + i["beginLesson"] + " " + i[
                            "dayOfWeekString"] + "  " + i["kindOfWork"] + "      " + i["discipline"] + "\n"
                        k[j] -= 1

            # Wensday
            if (k[j] > 0):
                if i["dayOfWeekString"] == "Ср":
                    if j == 2:
                        s_dat[2] += i["contentTableOfLessonsName"] + ")" + i["beginLesson"] + " " + i[
                            "dayOfWeekString"] + "  " + i["kindOfWork"] + "      " + i["discipline"] + "\n"
                        k[j] -= 1

            # Thersday

            if (k[j] > 0):
                if i["dayOfWeekString"] == "Чт":
                    if j == 3:
                        s_dat[3] += i["contentTableOfLessonsName"] + ")" + i["beginLesson"] + " " + i[
                            "dayOfWeekString"] + "  " + i["kindOfWork"] + "      " + i["discipline"] + "\n"
                        k[j] -= 1

            # Friday
            if (k[j] > 0):
                if i["dayOfWeekString"] == "Пт":
                    if j == 4:
                        s_dat[4] += i["contentTableOfLessonsName"] + ")" + i["beginLesson"] + " " + i[
                            "dayOfWeekString"] + "  " + i["kindOfWork"] + "      " + i["discipline"] + "\n"
                        k[j] -= 1

            # Saturday
            if (k[j] > 0):
                if i["dayOfWeekString"] == "Сб":
                    if j == 5:
                        s_dat[5] += i["contentTableOfLessonsName"] + ")" + i["beginLesson"] + " " + i[
                            "dayOfWeekString"] + "  " + i["kindOfWork"] + "      " + i["discipline"] + "\n"
                        k[j] -= 1

                # bot.send_message(message.chat.id,i_extra["dayOfWeekString"])
            # bot.send_message(message.chat.id,i["dayOfWeekString"])
        # s_dat[5]=s_mes
        # bot.send_message(message.chat.id,s_dat[5])

    for j in range(0, 6):
        if s_dat[j] != "":
            bot.send_message(message.chat.id, s_dat[j] + "\n" + "--------------------------------------")
        else:
            s_dat[j] = "Have a nice day, you have no lessons"
            bot.send_message(message.chat.id, s_dat[j] + "\n" + "--------------------------------------")

    bot.send_message(message.chat.id, "Have a nice week <3")
    bot.send_message(message.chat.id, 'Please, enter your group', reply_markup=markup)


bot.infinity_polling()



