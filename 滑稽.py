'''
/xyx
version -- 2.0
代码重构
'''

#导入
from turtle import *

		
def settings():
	hideturtle()
	setup(600,600,200,200)
	pensize(5)
	pass


def face():
	#脸
	penup()
	goto(-210,0)
	seth(-90)
	pendown()
	fillcolor('yellow')
	begin_fill()
	circle(210,360)
	end_fill()
	pass


def mouse():
	#嘴
	penup()
	goto(-150,-30)
	pendown()
	seth(-90)
	circle(150,180)
	pensize(2)
	pass


def eye_sockets():
	pass
	#眼眶
	#左上
	penup()
	pensize(4)
	goto(-180,90)
	pendown()
	seth(40)
	fillcolor('white')
	begin_fill()
	circle(-120,80)
	#左下
	penup()
	goto(-180,90)
	seth(-130)
	pendown()
	circle(15,110)
	seth(40)
	circle(-106,83)
	seth(30)
	circle(20,95)
	end_fill()
	#右上
	penup()
	goto(20,90)
	seth(40)
	pendown()
	fillcolor('white')
	begin_fill()
	circle(-120,80)
	#右下
	penup()
	goto(20,90)
	pendown()
	seth(-130)
	circle(15,110)
	seth(40)
	circle(-106,83)
	seth(30)
	circle(20,95)
	end_fill()
	pass


def eyes():
	#眼睛
	#左眼
	penup()
	goto(50,90)
	pendown()
	fillcolor('orange')
	begin_fill()
	circle(10,360)
	end_fill()
	#右眼
	penup()
	goto(-150,90)
	pendown()
	fillcolor('orange')
	begin_fill()
	circle(10,360)
	end_fill()
	pass


def main():
	#主程序
	'''

		运行顺序 :
			设置
			↓
			画脸
			↓
			画嘴
			↓
			画眼眶
			↓
			画眼睛
			↓
			Ojbk :)

	'''

	settings()
	face()
	mouse()
	eye_sockets()
	eyes()
	pass

	#我是不会忘记结束的 :)
	done()
	pass


#启动  ←_←
main()