# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 

# get your api_id, api_hash, token
api_id = 'YOUR API ID'
api_hash = 'YOUR API HASH'
token = 'YOUR BOT TOKEN'

# your phone number 
phone = 'YOUR_PHONE_NUMBER_WTH_COUNTRY_CODE'

# creating a telegram session and assigning 
# it to a variable client 
client = TelegramClient('session', api_id, api_hash) 

# connecting and building the session 
client.connect() 

# in case of script ran first time it will 
# ask either to input token or otp sent to 
# number or sent or your telegram id 
if not client.is_user_authorized(): 

	client.send_code_request(phone) 
	
	# signing in the client 
	client.sign_in(phone, input('Enter the code: ')) 


try: 


	# sending message using telegram client 
	client.send_message('USERNAME', 'message') 
except Exception as e: 

	# there may be many error coming in while like peer 
	# error, wwrong access_hash, flood_error, etc 
	print(e); 

# disconnecting the telegram session 
client.disconnect() 

# Refrence- https://www.geeksforgeeks.org/send-message-to-telegram-user-using-python/