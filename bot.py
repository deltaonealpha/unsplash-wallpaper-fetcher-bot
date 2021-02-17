########################################################
# Solid Snake Walls Bot
# a bot to automate media messages to the unsplashWallpaperDownloaderBot channel.
# written in async-logic with webhooks
#
# unsplashWallpaperDownloaderBot-bot version-0.1
# //deltaonealpha      
########################################################

#@restricted
#unsplashWallpaperDownloaderBot-BOT-master
API_TOKEN = "1683566389:AAHFlM98Q3ZekJkeeqvmh8JUPa-dzqvYqlY"
TOKEN = "1683566389:AAHFlM98Q3ZekJkeeqvmh8JUPa-dzqvYqlY"

allowedIDs = [680917769, 844398961]

import os
PORT = int(os.environ.get('PORT', 5000))

import telegram
from telegram.ext import Updater
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackContext

from datetime import datetime

from pathlib    import Path
from string     import ascii_letters, digits
from random     import choice
from os         import system, name
import os
from time       import sleep
from requests   import get

script_version  = '1.0'
script_title    = 'unsplash WP Downloader by ALIILAPRO (version {})'.format(script_version)

def start_script():
	print()

def genString(stringLength):
	letters = ascii_letters + digits
	return ''.join(choice(letters) for i in range(stringLength))

def req(url):
	try:
		r = get(url)
	except:
		r = get(url)
	return r

def download():
	try:
		start_script()
		DOWNLOAD_FOLDER = './wp'
		FILE_NAME       = 'unsplash-{}.jpg'.format(genString(7))
		FILE_PATH       = '{}/{}'.format(DOWNLOAD_FOLDER,FILE_NAME)
		BASE_URL        = 'https://source.unsplash.com'
		RES_URL         = '1920x1080'
		KEYWORDS        = ['HD Wallpapers', 'Experimental', 'hope', 'travel', 'dark']
		URL             = '{}/{}/?{}'.format(BASE_URL, RES_URL, choice(KEYWORDS))
		Path(DOWNLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
		print("[+] Start downloading...")
		img_data = req(URL).content
		with open(FILE_PATH, 'wb') as handler:
			handler.write(img_data)
		print("[+] Wallpaper [{}] successfully downloaded.".format(FILE_NAME))
		#FILE_NAME = str(FILE_NAME).replace("wpunsplash", "unsplash")
		#print(FILE_NAME)
		return(str(os.getcwd()+"\\wp\\"+FILE_NAME))
	except Exception as error:
		print(error)
		sleep(5)

updater = Updater(token=API_TOKEN, use_context=True)
j = updater.job_queue

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from functools import wraps
def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in allowedIDs:
            print("Unauthorized access denied for {}.".format(user_id))
            YOUR_CHAT_ID = user_id
            delSendText = ("Unauthorized access denied for "+str(user_id)+".")
            url = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
            data = {'chat_id': {YOUR_CHAT_ID}, 'text': delSendText}
            requests.post(url, data).json()
            return
        return func(update, context, *args, **kwargs)
    return wrapped

def start(update, context):
    now = datetime.now()
    context.bot.send_message(chat_id=update.effective_chat.id, text='''Unsplash Wallpaper Downloader bot\n
based on https://github.com/ALIILAPRO/unsplash-wallpaper-downloader\nBot by @deltaonealpha''')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

@restricted
def fetchwall(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Running process...")
    FILE_NAME = download()
    context.bot.sendDocument(chat_id=update.effective_chat.id, document=open(FILE_NAME, 'rb'))
    os.remove(FILE_NAME)
dispatcher.add_handler(CommandHandler("fetchwall", fetchwall))

#place this handler at the very end
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this is an invalid command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

print('''unsplashWallpaperDownloader-bot version-0.1
server:LAPTOP-1U6ES52S
users authorized: '''+str(len(allowedIDs))+"\n")

import time
print("%f " %  time.time())
print("check_scn:start")


updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=API_TOKEN)
updater.bot.setWebhook('https://lit-island-64859.herokuapp.com/' + TOKEN)


########################################################
# unsplashWallpaperDownloaderBot-bot version-0.1
# //deltaonealpha      
########################################################