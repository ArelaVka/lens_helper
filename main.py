#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import datetime
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello')
    logger.log(9, 'You call "Start" command')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help')
    logger.log(9, 'You call "Help" command')

def zamena(bot, update):
    """Save change date"""
    now = str(datetime.datetime.now())
    logger.log(9, 'You call "zamena" command and save "%s" as date', now)


def talking(bot, update):
    """Send a message to talk"""
    msg_txt = update.message.text
    if msg_txt == "время":
        now = datetime.datetime.now()
        update.message.reply_text(str(now))
    else:
        update.message.reply_text('I dont know!')
    logger.log(9, 'You call "talking" command')


# def echo(bot, update):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)
#     log_txt=update.message.text
#     logger.log(9, 'You say "%s" now, and I answer it', log_txt)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater('506471422:AAG70XKjvRxlElereskt5aCm5V1H_o_pNLw')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("zamena", zamena))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler(Filters.text, talking))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.level = 9
    main()
