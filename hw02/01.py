import csv
import re

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
main_data = ['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']
file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def write_to_csv(csv_file, file_list):
    get_data(file_list)
    data = [main_data]

    for i in range(0, len(file_list)):
        data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

    with open(csv_file, 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)

    with open(csv_file) as f_n:
        print(20*'*'+' результат ' + 20*'*')
        print(f_n.read())


def get_param(pattern, res_list, text):
    if re.match(pattern, text):
        res_list.append(re.sub(pattern, '', text).strip())


def get_data(file_list):
    for file_name in file_list:
        with open(file_name, encoding='Windows-1251') as f_n:
            for ln in f_n:
                get_param(r'Изготовитель ОС:\s+', os_prod_list, ln)
                get_param(r'Название ОС:\s+', os_name_list, ln)
                get_param(r'Код продукта:\s+', os_code_list, ln)
                get_param(r'Тип системы:\s+', os_type_list, ln)


write_to_csv('res.csv', file_list)





