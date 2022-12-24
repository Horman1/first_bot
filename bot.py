from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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

def guess_number(update, context):
    print(context.args)
    if context.args: #context.args - то что ввёл пользователь после команды /guess
        try:
            user_number = int(context.args[0])
            message = f' Ваше число {user_number}'
        except(TypeError, ValueError):
            message = 'Введите целое число'
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
