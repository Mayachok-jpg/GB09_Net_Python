# Программа клиента для отправки приветствия серверу и получения ответа
import argparse
import logging
import socket
import json
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

        presence_message_2_server = form_message_to_server('presence')
        client_socket.send(bytes(presence_message_2_server, encoding='utf-8'))

        message_from_server = client_socket.recv(640)
        check_server_message(message_from_server)

        client_socket.close()
    except ConnectionError:
        client_logger.critical('сервер не отвечает')


@Log()
def check_server_message(message):
    server_message = json.loads(message)
    # print(f'Received message from server: {server_message}')
    client_logger.info(f'получен ответ: {server_message}')


@Log()
def form_message_to_server(message_type: str):
    message = {
        "action": message_type,
        "time": time.ctime(time.time()),
        "type": "status",
        "user": {
            "account_name": "I_am_Your_CLIENT",
            "status": "Yep, I am here!"
        }
    }
    return json.dumps(message)


if __name__ == "__main__":
    client_logger.debug('клиент стартовал')
    args = argvparse()
    create_client_socket(args.address, args.port)


