'''
文件说明 : 登陆时验证
编写作者 : Chenyg
编写时间 : 2020年4月6日
'''
import easygui as g
import username
import password
import send_message
import  json
import turing

now_username = username.get_user()
now_password = password.get_password()
send_message.send_message_run()

def choice():
    choice = g.ccbox(msg = "START",
            choices = ("Land" , "Forget Password"))
    if choice:
        land()
    else:
        forget_password()

def land():
    global  username,password
    number_of_time = 1
    value = []
    value = g.multpasswordbox(msg = "Land( Press 'OK' to go to the next step )",
                              fields = ("Username : " , "Password : "))
    if value[0] == now_username and value[1] == now_password:
        g.msgbox("哈哈只有这一步是中文,我是Cyg,这个程序是我一个人编写出来的,有什么报错给我说下哈,启动turing机器人")
        turing.turing()
    elif value[0] != now_username:
        choice = g.msgbox("Username error , do you want to tyr again?")
        if choice and number_of_time <= 2:
            number_of_time += 1
    else:
        choice = g.ccbox(msg = "Password error, do you want to try again?")
        if choice and number_of_time <= 2:
            number_of_time += 1

        else:
            forpassword = g.ccbox(msg = "Forget Password?",
                    choices = ("Yes" , "No"))
            if  forpassword:
                forget_password()
            else:
                g.msgbox("See you next time!")

def forget_password():
    new_username = g.enterbox("Enter your new username : ")
    new_password = g.enterbox("Enter you new password : ")
    new_email = g.enterbox("Enter your new emali address : ")
    msg = send_message.send_message(new_email)
    if msg:
        with open("username.json",'w') as f_obj:
            json.dump(new_username,f_obj)
        with open("password.json",'w') as p_obj:
            json.dump(new_password,p_obj)
        with open("email_address.json",'w') as e_obj:
            json.dump(new_email,e_obj)
        g.msgbox("Changed data successfully ")
        land = g.ccbox(msg = "Do you want to log in now?")
        if land:
            land()
        else:
            g.msgbox("See you next time!")


choice()




