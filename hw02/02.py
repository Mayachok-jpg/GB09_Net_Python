import json


def get_data(file_name):
    with open(file_name) as f_n:
        objs = json.load(f_n)
    return objs


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = get_data('orders.json')
    dict_to_json['orders'].append([item, quantity, price, buyer, date])

    with open('orders.json', 'w') as f_n:
        json.dump(dict_to_json, f_n, indent=4)


print(get_data('orders.json'))
write_order_to_json('торт', 10, '45р', 'таня', '18.12.81')
print(get_data('orders.json'))
