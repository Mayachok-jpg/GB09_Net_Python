# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
import logging
import socket
import json
import sys
import time
from log import client_log_config
from decorators import Log

client_logger = logging.getLogger('clientLogger')


@Log()
def argvparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default='localhost')
    parser.add_argument('-p', '--port', type=int, default=7777)

    return parser.parse_args()


@Log()
def create_client_socket(address, port=7777):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создать сокет TCP

    try:
        client_socket.connect((address, port))  # Соединиться с сервером

        client_logger.info('соединение установлено')


        presence_message_to_server = form_message_to_server('presence', client_socket)
        client_socket.send(bytes(presence_message_to_server, encoding='utf-8'))

        message_from_server = client_socket.recv(640)
        check_server_message(message_from_server)
        client_logger.info('соединение установлено')
        # client_socket.close()

    except ConnectionError:
        client_logger.critical('сервер не отвечает')
    else:
        while True:
            try:
                check_server_message(message_from_server)
            except:
                client_logger.error(f'Соединение с сервером {address} было потеряно.')
                sys.exit(1)

@Log()
def check_server_message(message):
    server_message = json.loads(message)
    print(f'Received message from server: {server_message}')
    if server_message['response'] == '200':
        client_logger.info(f'получен ответ: {server_message}')
        print(f'получен ответ: {server_message}')


@Log()
def form_message_to_server(message_type: str, client_socket):
    if message_type == 'presence':
        message = {
            "action": message_type,
            "time": time.ctime(time.time()),
            "type": "status",
            "user": {
                "account_name": "I_am_Your_CLIENT",
                "status": "Yep, I am here!"
            }
        }
    elif message_type == 'user_message':
        user_text = input('Введите сообщение для отправки или \'q\' для завершения работы: ')
        if user_text == 'q':
            client_socket.close()
            print('Завершение работы')
            sys.exit(0)

        message = {
            "action": message_type,
            "time": time.ctime(time.time()),
            "type": "text",
            "user": {
                "account_name": "Guest",
                "status": "Yep, I am here!"
            },
            "text": user_text
        }
    return json.dumps(message)


if __name__ == "__main__":
    client_logger.debug('клиент стартовал')
    print('начинаем работу')
    args = argvparse()
    create_client_socket(args.address, args.port)


