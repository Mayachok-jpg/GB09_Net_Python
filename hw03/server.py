# Программа сервера для получения приветствия от клиента и отправки ответа
import logging
import select
import socket
import time
import json
import argparse
from log import server_log_config
from decorators import log

server_logger = logging.getLogger('serverLogger')


@log
def argvparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', default='')
    parser.add_argument('-p', '--port', type=int, default=7777)

    return parser.parse_args()


@log
def create_server_socket(address='', port=7777):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создает сокет TCP
    server_socket.bind((address, port))                                  # Присваивает порт
    server_socket.settimeout(0.5)                                              # Переходит в режим ожидания запросов;
    server_logger.debug('сокет создан')                                  # Одновременно обслуживает не более
                                                                         # 5 запросов.
    clients = []
    messages = []

    server_socket.listen(5)

    while True:
        try:
            client, addr = server_socket.accept()
        except OSError:
            pass
        else:
            server_logger.info(f'поступил запрос от клиента {addr}')
            clients.append(client)

        recv_data_lst = []
        send_data_lst = []
        err_lst = []

        try:
            if clients:
                recv_data_lst, send_data_lst, err_lst = select.select(clients, clients, [], 0)
        except OSError:
            pass

        #         тут рыбы нет

        if recv_data_lst:
            for client_with_message in recv_data_lst:
                try:
                    data = client_with_message.recv(640)
                    if not data:
                        server_logger.warning(f'не пришли данные от {addr}')
                    message_from_client = check_client_message(data, addr)
                    messages.append((addr, message_from_client))

                    print(message_from_client)
                    print(f' Список сообщений {messages}')
                    print(f' адрес {messages[0][0]}')
                    print(f' сообщение {messages[0][1]}')

                except:
                    server_logger.info(f'клиент {client_with_message.getpeername()} отключился от сервера.')
                    clients.remove(client_with_message)

                if messages and send_data_lst:
                    for waiting_client in send_data_lst:
                        try:
                            # отправить сообщение клиенту
                            message_to_client = form_response_to_client(messages[0])
                            waiting_client.send(bytes(message_to_client, encoding='utf-8'))
                            del messages[0]
                        except:
                            server_logger.info(f'клиент {waiting_client.getpeername()} отключился от сервера.')
                            clients.remove(waiting_client)

        #         тут рыбы нет


'''
        message_from_client = check_client_message(data, addr)
        message_to_client = form_response_to_client(message_from_client)

        client.send(bytes(message_to_client, encoding='utf-8'))
        client.close()
'''

@log
def check_client_message(message: json, address: str) -> tuple:

    client_message = json.loads(message)

    # print(f'"action" message from client {address}: {client_message["action"]}')
    server_logger.info(f'получено сообщение от клиента {client_message["user"]}, {client_message["text"]}')
    return client_message['action'], client_message['user'], client_message["text"]


@log
def form_response_to_client(message_from_client):
    response = ''

    if message_from_client[1][0] == 'presence':
        response = '100'


    if message_from_client[1][0] == 'user_message':
        response = '200'

    message = {
        "response": response,
        "time": time.ctime(time.time()),
        "text": message_from_client[1][1]
    }

    return json.dumps(message)


if __name__ == "__main__":
    server_logger.info('cервер запущен')
    args = argvparse()
    create_server_socket(args.address, args.port)