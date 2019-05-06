from config import *
from flask import request
from flask import Flask
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEvent, VkBotEventType
import logging
from random import randint



app = Flask(__name__)

 
# add filemode="w" to overwrite
logging.basicConfig(filename="requests.log", level=logging.INFO)

@app.route('/confirm', methods=['POST'])
def confirmation():
    return CHECK_RESPONSE

session = vk_api.VkApi(token=ACCESS_KEY)
longpoll = VkBotLongPoll(vk=session, group_id=GROUP_ID)
vk = session.get_api()

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
		if event.from_user:
			random_id = randint(-214748369, 2147483647)
			vk.messages.send(
				user_id=event.obj.from_id,
				random_id=random_id,
				message='Ну ок'
			)
		if event.from_chat:
			random_id = randint(-214748369, 2147483647)
			vk.messages.send(
				chat_id=event.chat_id,
				random_id=random_id,
				message='Ага'
			)
	elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
		random_id = randint(-214748369, 2147483647)
		vk.messages.send(
			user_id=event.obj.from_id,
			random_id=random_id,
			message='Давай быстрее'
		)
