#!/usr/bin/python3

# 方法定义
def printme(str):
	"打印传入的参数"
	print(str)
	return

# 方法调用
printme("hello world")

print("*****************参数传递 START***********************")
a = 1
# 传递不可变对象
def changeme1(a):
	a = 2
	print("方法内a = ", a)
	return

# 输出
# 方法内a =  2
# 方法外a =  1
changeme1(a)
print("方法外a = ", a)

b = [1, 2, 3]
# 传递可变对象
def changeme2(b):
	b.append([4, 5, 6])
	print("方法内b = ", b)
	return
# 输出
# 方法内b =  [1, 2, 3, [4, 5, 6]]
# 方法外b =  [1, 2, 3, [4, 5, 6]]
changeme2(b)
print("方法外b = ", b)

print("*****************参数传递 END***********************")

print("*****************关键字参数 START***********************")
def printscore(name, score):
	print("学生：", name, "，分数：", score)
	return

stu = "小明"
mathScore = 99
# 输出 学生： 小明 ，分数： 99
printscore(stu, mathScore)
# 输出 学生： 小明 ，分数： 100
printscore(score=mathScore + 1, name=stu)
print("*****************关键字参数 END***********************")

print("*****************默认参数 START***********************")
def printAge(name, age = 10):
	print("学生：", name, "年龄：", age)
	return
# 输出 学生： 小明 年龄： 12
printAge("小明", 12)
# 输出 学生： 小红 年龄： 10
printAge("小红")
print("*****************默认参数 END***********************")

print("*****************不定长参数 START***********************")
def printFamily(father, *others):
	print("户主：", father)
	print("其他人：")
	for name in others:
		print(name)
# 输出
# 户主： father
# 其他人：
printFamily("father")

# 输出
# 户主： father
# 其他人：
# mather
# brother
printFamily("father", "mather", "brother")
print("*****************不定长参数 END***********************")

print("*****************lambda匿名函数 START***********************")
sum = lambda n1, n2, n3: n1+n2+n3
# 输出6
print("求和：", sum(1, 2, 3))
print("*****************lambda匿名函数 END***********************")
