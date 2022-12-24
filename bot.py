from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(update, context):
    text = 'Бот запущен'
    logging.info(text)
    update.message.reply_text(
        f'{text}. Привет {update.message.chat.username}, как жизнь?')


def talk_to_me(update, context):
    user_text = "Hello {}, я интерактивный Telegram Bot".format(update.message.chat.username)
    print(update.message)
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
    update.message.reply_text(message)


def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # Обработчик сообщений от юзера

    mybot.start_polling()
    mybot.idle()


main()
