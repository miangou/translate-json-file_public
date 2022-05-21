import random
import hashlib

import requests
import json

api = ''
app_id = ''
app_key = ''
str_from = 'auto'
to = 'zh'


def md5_maker(q: str):
    # q.encode(encoding='UTF-8')
    salt = str(random.randint(1, 100000))
    sign = app_id + q + salt + app_key
    return_md5 = hashlib.md5()
    return_md5.update(sign.encode('UTF-8'))
    sign = return_md5.hexdigest()
    return_list = [sign, salt]
    return return_list


def back_value(q: str):
    need_list = md5_maker(q)
    data = {
        'q': q,
        'from': str_from,
        'to': to,
        'appid': app_id,
        'salt': need_list[1],
        'sign': need_list[0]
    }
    back = requests.get(api, data)
    back.encoding = 'utf-8'
    back_json = back.json()
    return back_json['trans_result'][0]['dst']


def file_read(a: str):
    with open(a, "r") as file:
        file_json = json.load(file)  # 剩下的就是解析了，都是列表和字典的操作
    print(file_json)
    for key, value in file_json.items():
        file_json[key] = back_value(value)
    file.close()
    with open(a + "_translated.json", 'w+') as file:
        json.dump(file_json, file,ensure_ascii=False)


path = input("请把文件拖进来并按回车-_-:")
file_read(path)
