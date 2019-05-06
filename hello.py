from config import *
from flask import request
from flask import Flask
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import logging
from random import randint



app = Flask(__name__)

 
# add filemode="w" to overwrite
logging.basicConfig(filename="requests.log", level=logging.INFO)

@app.route('/confirm', methods=['POST'])
def confirmation():
    return CHECK_RESPONSE

session = vk_api.VkApi(token=ACCESS_KEY)
longpoll = VkLongPoll(session)
vk = session.get_api()

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
		if event.from_user:
			random_id = randint(-214748369, 2147483647)
			vk.messages.send(
				user_id=event.user_id,
				random_id=random_id,
				message='Ну ок'
			)
	elif event.type == VkEventType.USER_TYPING:
		random_id = randint(-214748369, 2147483647)
		vk.messages.send(
			user_id=event.user_id,
			random_id=random_id,
			message='Давай быстрее'
		)
