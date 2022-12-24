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
         f'{text}. Привет {update.message.chat.username}, это персональный бот Кири, который спросит с тебя за базар.')

def talk_to_me(update, context):
    user_text = "Привет {}, я интерактивный Telegram Bot".format(update.message.chat.username)
    print(update.message)
    logging.info('User: %s, Chat_id: %s, Message: %s', update.message.chat.username, update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Бот запускается')

    #dp = Updater(settings.API_KEY).dispatcher
    Updater(settings.API_KEY).dispatcher.add_handler(CommandHandler("start", greet_user))
    Updater(settings.API_KEY).dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))# Обработчик сообщений от юзера

    Updater(settings.API_KEY).start_polling()
    Updater(settings.API_KEY).idle()


main()
