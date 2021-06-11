import fh_parser
from time import sleep
import telebot

bot = telebot.TeleBot("1024618614:AAFeRLIWblOLZRhtQLT06L5G2biUV09yWwQ")


@bot.message_handler(commands=['start'])
def start_mes(mes):
    old_projects = set()
    while True:
        projects = fh_parser.parse_projects()
        new_projects = set(projects) - old_projects
        if new_projects:
            for project in new_projects:
                url = project.get_attribute_list('href')[0]
                description = project.get_attribute_list('title')[0]
                markup = telebot.types.InlineKeyboardMarkup()
                btn = telebot.types.InlineKeyboardButton(text='Перейти', url=f'{url}')
                markup.add(btn)
                bot.send_message(mes.chat.id, f'🧑🏼‍💻<b>{project.text}</b>🧑🏼‍💻\n\n{description}',
                                 reply_markup=markup,
                                 parse_mode='html')
        old_projects = set(projects)
        sleep(10)


bot.polling()
