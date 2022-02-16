# Программа сервера для получения приветствия от клиента и отправки ответа
import logging
import socket
import time
import json
import argparse
from log import server_log_config

server_logger = logging.getLogger('serverLogger')

def argvparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default='')
    parser.add_argument('-p', '--port', type=int, default=7777)

    return parser.parse_args()


def create_server_socket(address='', port=7777):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создает сокет TCP
    server_socket.bind((address, port))                                  # Присваивает порт
    server_socket.listen(5)                                              # Переходит в режим ожидания запросов;
    server_logger.debug('сокет создан')                                  # Одновременно обслуживает не более
                                                                         # 5 запросов.

    while True:
        client, addr = server_socket.accept()
        server_logger.info(f'поступил запрос от клиента {addr}')
        # print(f'accept request from client {addr}')

        data = client.recv(640)
        if not data:
            server_logger.warning(f'не пришли данные от {addr}')
            #print(f"we don't received any data from {addr}")

        message_from_client = check_client_message(data, addr)
        message_to_client = form_response_to_client(message_from_client)

        client.send(bytes(message_to_client, encoding='utf-8'))
        client.close()


def check_client_message(message: json, address: str) -> tuple:

    client_message = json.loads(message)

    # print(f'"action" message from client {address}: {client_message["action"]}')
    server_logger.info(f'получено сообщение от клиента {client_message["user"]}')
    return client_message['action'], client_message['user']


def form_response_to_client(message_from_client):
    response = ''

    if message_from_client[0] == 'presence':
        response = '100'

    message = {
        "response": response,
        "time": time.ctime(time.time()),
    }
    return json.dumps(message)


if __name__ == "__main__":
    server_logger.info('cервер запущен')
    args = argvparse()
    create_server_socket(args.address, args.port)