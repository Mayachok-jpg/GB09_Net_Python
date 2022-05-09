import logging
from logging import handlers

log_path = 'test_server_log.log' if __name__ == "__main__" else 'log/server.log'

format = logging.Formatter('%(levelname)-10s %(asctime)s %(module)s %(message)s')

server_logger = logging.getLogger('serverLogger')
server_logger.setLevel(logging.DEBUG)

# ежедневная ротация нужна на стороне сервера
server_file_log = logging.handlers.TimedRotatingFileHandler(log_path, 'midnight')
server_file_log.setFormatter(format)

server_logger.addHandler(server_file_log)

if __name__ == "__main__":

    server_logger.info('информационное сообщение')
    server_logger.critical('все пропало')
