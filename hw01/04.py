str_list = ['разработка', 'администрирование', 'protocol', 'standard']

def print_els(print_list):
    for el in print_list:
        b_el = el.encode('utf-8')
        str_el = b_el.decode('utf-8')

        print(f' Содержание переменной: {el}, байтовое представление: {b_el}, обратное преобразование, {str_el}')


print_els(str_list)

