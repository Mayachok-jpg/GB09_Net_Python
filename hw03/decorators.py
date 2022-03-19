import inspect
import logging
import sys
from functools import wraps

if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('serverLogger')
else:
    LOGGER = logging.getLogger('clientLogger')


class Log:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            wraps(func)
            result = func(*args, **kwargs)
            LOGGER.debug(f'Функция: {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
            return result
        return wrapper


def log(func):
    def wrapper(*args, **kwargs):
        wraps(func)
        result = func(*args, **kwargs)
        LOGGER.debug(f'Функция: {func.__name__} вызвана из функции {inspect.stack()[1][3]}')
        return result
    return wrapper


