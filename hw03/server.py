# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='')
parser.add_argument('-p', '--port', type=int, default=7777)


args = parser.parse_args()
# print(f'addr {args.addr} {type(args.addr)} port {args.port} {type(args.port)}')


s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((args.addr, args.port))    # Присваивает порт
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более
                                  # 5 запросов.
while True:
    client, addr = s.accept()
    data = client.recv(1000000).decode('utf-8')
    data_dict = json.loads(data)
    print('Сообщение: ', data, ', было отправлено клиентом: ', addr)

    if data_dict['action'] == 'presence':
        answer = {
        "response": 200,
        "alert":"Необязательное сообщение/уведомление",
        "time": time.ctime(time.time()),
        }
    else:
        answer = 'Чет не понял'

    msg = json.dumps(answer)

    client.send(msg.encode('utf-8'))
    client.close()