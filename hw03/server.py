# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import json
import argparse


def argvparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default='')
    parser.add_argument('-p', '--port', type=int, default=7777)

    return parser.parse_args()


def dec_message(data, addr):

    data_dict = json.loads(data)
    print('Сообщение: ', data, ', было отправлено клиентом: ', addr)
    return data_dict


def enc_message(data_dict):
    if data_dict['action'] == 'presence':
        answer = {
        "response": 200,
        "alert":"Необязательное сообщение/уведомление",
        "time": time.ctime(time.time()),
        }
    else:
        answer = {
        "response": 400,
        "alert":"Неправильный запрос/JSON-объект",
        "time": time.ctime(time.time()),
        }

    print(answer)
    msg = json.dumps(answer)
    return msg


def main():

    args = argvparse()
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind((args.addr, args.port))    # Присваивает порт
    s.listen(5)                       # Переходит в режим ожидания запросов;
                                      # Одновременно обслуживает не более
                                      # 5 запросов.
    while True:
        client, addr = s.accept()
        data = client.recv(1000000).decode('utf-8')
        data_dict = dec_message(data, addr)
        msg = enc_message(data_dict)
        client.send(msg.encode('utf-8'))
        client.close()


if __name__ == "__main__":
    main()