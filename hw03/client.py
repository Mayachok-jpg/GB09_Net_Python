# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
from socket import *
import json
import time


def argvparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--addr', default='localhost')
    parser.add_argument('-p', '--port', type=int, default=7777)

    return parser.parse_args()


def enc_message(message_type):
    msg = {
                "action": message_type,
                "time": time.ctime(time.time()),
                "type": "status",
                "user": {
                        "account_name": "C0deMaver1ck",
                        "status": "Yep, I am here!"
                }
    }

    return json.dumps(msg)


def dec_message(data):

    data_dict = json.loads(data)
    return data_dict


def main():
    args = argvparse()

    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((args.addr, args.port))   # Соединиться с сервером

    msg = enc_message('presence')

    s.send(msg.encode('utf-8'))
    data = s.recv(1000000).decode('utf-8')
    data_dict = dec_message(data)
    print('Сообщение от сервера: ', data_dict, ', длиной ', len(data), ' байт')
    if data_dict['response'] == 200:
        print('сервер сказал, что все прошло хорошо')
    s.close()

if __name__ == "__main__":
    main()