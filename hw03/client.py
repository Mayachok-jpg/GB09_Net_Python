# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *
import json
import time
import sys

addr = 'localhost'
port = 7777

if len(sys.argv) > 1:
        addr = sys.argv[1]
if len(sys.argv) > 2:
        port = int(sys.argv[2])

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((addr, port))   # Соединиться с сервером

presens_msg = {
        "action": "presence",
        "time": time.ctime(time.time()),
        "type": "status",
        "user": {
                "account_name":  "C0deMaver1ck",
                "status":      "Yep, I am here!"
        }
}

msg = json.dumps(presens_msg)


s.send(msg.encode('utf-8'))
data = s.recv(1000000).decode('utf-8')
data_dict = json.loads(data)
print('Сообщение от сервера: ', data_dict, ', длиной ', len(data), ' байт')
if data_dict['response'] == 200:
        print('сервер сказал, что все прошло хорошо')
s.close()
