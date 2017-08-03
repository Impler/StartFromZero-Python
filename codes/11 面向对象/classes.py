#!/bin/bash/python3

class People:
	## --- 成员变量 ---
	# 公有成员变量
	name = ''
	age = 0
	# 私有成员变量
	# 变量名以'__'开头
	__incoming = 0

	## --- 成员方法 ---
	## 使用def关键字，且第一个参数必须为self（也可以为别的名字），表示当前对象
    ## python方法不支持重载，但可以通过缺省参数来实现类似的功能
	# 私有方法，方法名以'__'开头
	# __init__()为类的专有方法，相当于构造函数
	def __init__(self, name='', age=0, incoming=0):
		self.name = name
		self.age = age
		self.__incoming = incoming

    # 公有方法
	def print(self):
		print("people name=%s, age=%s, incoming=%d" %(self.name, self.age, self.__incoming))

# 使用缺省参数
p1 = People()
# 输出people name=, age=0, incoming=0
p1.print()
# 传参
p2 = People("张三", 20) 
# 输出 people name=张三, age=20, incoming=0
p2.print()
# 调用共有成员
# 输出 name=张三
print("name=%s" %(p2.name))
# 输出 age=20
print("age=%d" %(p2.age))

# 调用私有成员
# 输出 私有方法不可访问
try:
    p2.__incoming
except :
	print("私有方法不可访问")