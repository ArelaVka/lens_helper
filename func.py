#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import datetime

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
