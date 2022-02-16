import logging
from logging import handlers

log_path = 'test_log.log' if __name__ == "__main__" else 'log/client.log'

# logging.basicConfig(
#     # filename=log_path,
#     format='%(asctime)s %(levelname)-10s %(module)s %(message)s',
#     level=logging.INFO
# )

format = logging.Formatter('%(levelname)-10s %(asctime)s %(module)s %(message)s')

client_logger = logging.getLogger('clientLogger')
client_logger.setLevel(logging.DEBUG)

client_file_log = logging.FileHandler(log_path)
client_file_log.setFormatter(format)

client_logger.addHandler(client_file_log)

# ежедневная ротация нужна на стороне сервера
# client_log.addHandler(handlers.TimedRotatingFileHandler(log_path, 'midnight'))
# client_log.setFormatter(format)


if __name__ == "__main__":
    # logging.basicConfig(
    #     filename='client.log'
    # )
    client_logger.info('информационное сообщение')
    client_logger.critical('все пропало')
