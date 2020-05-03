'''
文件说明 : 处理用户登入信息
编写作者 : Chenyg
编写时间 : 2020年4月5日
'''

import json
import easygui as g

filename = 'username.json'

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = g.enterbox("What's your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)

def get_user():
    global username
    username = get_stored_username()
    if username:
        pass
    else:
        username = get_new_username()
    return username



