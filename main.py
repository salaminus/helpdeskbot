# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import jsonify
import json
import config
from requestBD import queryDB
import requests
from flask_sslify import SSLify


app = Flask(__name__)
#sslify = SSLify(app)

botToken = config.token
URL = 'http://sch1532uz.mskobr.ru'
URLbot = 'https://api.telegram.org/bot' + botToken + '/'


def messagesDB(message):  # Название функции не играет никакой роли, в принципе
    """ Запрос в БД и получение данных по запросу"""
    msg = message
    messageBot = queryDB(msg)[0]
    imageLink = queryDB(msg)[1]
    if len(messageBot) != 0:
        if not (len(messageBot) > 1):
            if len(imageLink[0][0]) != 0:   # если есть фото
                text = messageBot[0][0] + '\n'+ messageBot[0][1] + '\n' + URL + imageLink[0][0]
            else:                           # если нет фото
                text = messageBot[0][0] + '\n' + messageBot[0][1] + '\n' + 'Нет фото'
        else:
            text = 'Ваш запрос не точен.\nПопробуйте ввести фамилию и имя'
            #""" ---Проблема с однофамильцами!!!--- """
    else:
        text = 'По Вашему запросу нет данных'
    return (text)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        if message != None:
            text = messagesDB(message)
            send_message(chat_id, text=text)
        #write_json(r)
        return jsonify(r)
    else:
        return '<h1>Bot ready!</h1>'


def write_json(data, filename = 'answer.json'):
    """Получение json данных в файл"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2,
                  ensure_ascii=False)


def get_updates():
    """ Запрос обновлений в чате бота https://api.telegram.org/bot504306281:secret_Token/getUpdates"""
    url = URLbot + 'getUpdates'
    r = requests.get(url)
    #write_json(r.json())
    return r.json()


def send_message(chat_id, text):
    """Отправка сообщений в чат бота"""
    url = URLbot + 'sendMessage'
    answer = {  # словарь для передачи методом post
                'chat_id': chat_id,
                'text': text
             }
    r = requests.post(url, json = answer)
    return r.json()


def main():
    pass


if __name__ == '__main__':
    app.run()
