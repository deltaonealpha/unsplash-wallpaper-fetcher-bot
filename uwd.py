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
		os.startfile(str(os.getcwd()+"\\wp\\"+FILE_NAME))
		update.message.sendDocument(chat_id=update.effective_chat.id, document=open((str(os.getcwd()+"\\wp\\"+FILE_NAME)), 'rb'))
		os.remove(str(os.getcwd()+"\\wp\\"+FILE_NAME))
	except Exception as error:
		print(error)
		sleep(5)


run()

