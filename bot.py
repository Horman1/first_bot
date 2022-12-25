from emoji import emojize  # emojize - функция которая превращает текстовые изображения emoji в иконку эмоции.
from glob import glob
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def get_smile():
    smile = choice(settings.USER_EMOJI)  # Берем случайный смайлик из списка settings
    smile = emojize(smile, language='alias')  #Используем функцию emojize в которую передаем переменную smile,
    # указываем что случайно выбранный текст смайла надо преобразовать в иконку смайла
    # alias - так называются текстовые обозначения смайликов
    return smile

def greet_user(update, context):
    text = 'Бот запущен'
    smile = get_smile()
    logging.info(text)  #
    update.message.reply_text(
        f'{text}. Привет {update.message.chat.username}, как жизнь {smile}?')

def talk_to_me(update, context):
    user_text = "Hello {}, я интерактивный Telegram Bot".format(update.message.chat.username)
    print(update.message.text)
    print(user_text)
    logging.info('User: %s, Chat_id: %s, Message: %s', update.message.chat.username, update.message.chat.id,
                 update.message.text)
    update.message.reply_text(user_text)


def random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    print(bot_number)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы выиграли.'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, ничья.'
    else:
        message = f"Ваше число {user_number}, моё число {bot_number}, я выиграл."
    return message

def guess_number(update, context):
    print(context.args)  # context.args - то что ввёл пользователь после команды /guess
    if context.args:  # если context.args вообще есть в сообщении от пользователя, то далее:
        try:
            user_number = int(context.args[0])
            message = random_number(user_number)
        except(TypeError, ValueError):
            message = 'Введите целое число, а не ебанину'
    else:
        message = 'Введите число:'
    update.message.reply_text(message)  # Ответить в тот же чат в который написали.

def send_mem_image(update, context):
    mem_image_list = glob('images/*.jpg')  # Кладем в переменную список картинок подходящих под шаблон.
    mem_pic_filename = choice(mem_image_list)  # Кладем в переменную одну картинку на выбор.
    chat_id = update.effective_chat.id  # id чата с текущим пользователем
    context.bot.send_photo(chat_id=chat_id, photo=open(mem_pic_filename, 'rb'))  # Функция send_photo объекта bot в
    # context. Отправляет картинку пользователю. 'rb' формат read binary.
    # Для отправки картинки мы должны в явном виде указать чат пользователя, которому мы хотим отправить картинку.
    # Картинка - это бинарный двоичный формат.


def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("mem", send_mem_image))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # Обработчик сообщений от юзера

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
        main()
