'''
文件说明 : 处理用户密码
编写作者 : Chenyg
编写时间 : 2020年4月5日
'''
import json
import easygui as g

filename = 'password.json'

def get_stored_password():
    filename = 'password.json'
    try:
        with open(filename) as f_obj:
            password = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return password

def get_new_password():
    password = g.enterbox("Please enter your password : ")
    filename = 'password.json'
    with open(filename,'w') as f_obj:
        json.dump(password,f_obj)
        g.msgbox("We'll remember your name & password when you come back!")

def get_password():
    global password
    password = get_stored_password()
    if password:
        pass
    else:
        password = get_new_password()
    return password



