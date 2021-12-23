import yaml

action_list = ['msg_1',
          'msg_2',
          'msg_3']

to_list = 3

three = {12: '€'}

data_to_yaml = {'action':action_list, 'to':to_list, 'three': three}

with open('data_write.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_to_yaml, f_n, allow_unicode = True, default_flow_style=False)

with open('data_write.yaml', encoding='utf-8') as f_n:
    print(f_n.read())

