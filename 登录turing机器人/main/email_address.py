'''
文件说明 : 处理用户email address
编写作者 : Chenyg
编写时间 : 2020年4月5日
'''
import json
import easygui as g

filename = 'email_address.json'

def get_stored_email_address():
    filename = 'email_address.json'
    try:
        with open(filename) as f_obj:
            address = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return address

def get_new_email_addres():
    address = g.enterbox("We need your email to send the verification code : ")
    filename = 'email_address.json'
    with open(filename,'w') as f_obj:
        json.dump(address,f_obj)
        g.msgbox("We'll send the verification code!")
    return address

def get_email_address():
    address = get_stored_email_address()
    if address:
        address = get_stored_email_address()
        return address
    else:
        address = get_new_email_addres()
        return address


get_email_address()

