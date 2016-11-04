#!/usr/bin/python3

print ("常见数据类型：")
age = 100
size = 10.0
name = 'Tom'

print (age)
print (size)
print (name)

# ------------------
print ("字符类型：")
str = "hello world"

print (str)                     # 打印字符串
print (str[0])					# 打印第一个字符 						
print (str[2:4])				# 打印第3到第5个字符，左闭右开区间[2,4)，不存在下标越界。。。。
print (str[2])					# 打印第三个及以后的字符	
print (str * 3)					# 打印三遍
print (str + ' hello python')   # 拼接

# ------------------
print ("List类型：")
list = ['a', 1, 'c', 2, 4]
alist = ['b', 'c']
			
print (list)					# 打印list
print (list[0])				
print (list[1:7])
print (list[2:])
print (list * 2)
print (list + alist)