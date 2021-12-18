str_list = ['разработка', 'сокет', 'декоратор']
utf_list = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']


def print_els(print_list):
    for el in print_list:
        print(f' Содержание переменной: {el}, тип: {type(el)}')


print_els(str_list)
print_els(utf_list)


