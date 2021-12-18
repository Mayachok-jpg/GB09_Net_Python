utf_list = [b'\u0063\u006c\u0061\u0073\u0073', b'class', b'function', b'method']


def print_els(print_list):
    for el in print_list:
        print(f' Содержание переменной: {el}, тип: {type(el)}, длина {len(el)} ')


# print_els(str_list)
print_els(utf_list)

