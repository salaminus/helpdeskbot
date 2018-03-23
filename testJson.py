import json
import requests

"""Запрос https://api.telegram.org/bot504306281:AAHbh_Bq3JzqAOu7CcM68b6EQ5rI1EZfuTk/getMe"""
# r = requests.get(URLbot + 'getMe')
# write_json(r.json())

URL = 'https://api.telegram.org/bot504306281:AAHbh_Bq3JzqAOu7CcM68b6EQ5rI1EZfuTk/'


def write_json(data, filename = 'answer.json'):
    """Получение json данных в файл"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2,
                  ensure_ascii=False)


def get_updates():
    """ Запрос обновлений в чате бота https://api.telegram.org/bot504306281:AAHbh_Bq3JzqAOu7CcM68b6EQ5rI1EZfuTk/getUpdates"""
    url = URL + 'getUpdates'
    r = requests.get(url)
    #write_json(r.json())
    return r.json()


def send_message(chat_id, text = 'Test'):
    """Отправка сообщений в чат бота"""
    url = URL + 'sendMessage'
    answer = {  # словарь для передачи методом post
                'chat_id': chat_id,
                'text': text
             }
    r = requests.post(url, json = answer)
    return r.json()


def main():
    """Запрос https://api.telegram.org/bot504306281:AAHbh_Bq3JzqAOu7CcM68b6EQ5rI1EZfuTk/getMe"""
    r = requests.get(URL + 'getMe')
    write_json(r.json())

if __name__ == '__main__':
    # main()
    r = get_updates()
    # Распарсить ответ от Telegram:
    chat_id = r['result'][-1]['message']['chat']['id']
    send_message(chat_id, 'Текст')