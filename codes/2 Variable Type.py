#!/usr/bin/python3

print ("常见数据类型：")
age = 100
size = 10.0
name = 'Tom'

print (age)
print (size)
print (name)

# ------------------
print ("------------")
print ("字符类型：")
str = "hello world"

print (str)                     # 打印字符串
print (str[0])					# 打印第一个字符 						
print (str[2:4])				# 打印第3到第5个字符，左闭右开区间[2,4)，不存在下标越界。。。。
print (str[2])					# 打印第三个及以后的字符	
print (str * 3)					# 打印三遍
print (str + ' hello python')   # 拼接

# ------------------
print ("------------")
print ("List类型：")
list = ['a', 1, 'c', 2, 4]
alist = ['b', 'c']
			
print (list)					# 打印list
print (list[0])					# 打印第一个元素
print (list[1:7])				# 打印第二到八个元素
print (list[2:])				# 从第三个元素开始打印
print (list * 2)				# 重复打印两遍
print (list + alist)			# 两个集合拼接

# ------------------
print ("------------")
print ("Tuple类型：")
tuple = ('a', 1, 'c', 2, 4)
atuple = ('b', 'c')

print (tuple)					# 打印tuple
print (tuple[0])				# 打印第一个元素
print (tuple[1:7])				# 打印第二到八个元素
print (tuple[2:])				# 从第三个元素开始打印
print (tuple * 2)				# 重复打印两遍
print (tuple + atuple)			# 两个tuple拼接

# list的元素可以随意改变
print ("原list：")
print (list)
list[0] = 2
print ("修改后list：")
print (list)

# tuple的元素不可改变
# TypeError: 'tuple' object does not support item assignment
# tuple[0] = 2

#--------------------
print ("------------")
print ("Dictionary类型：")

dict = {"k1": "v1", "k2":1}
dict['one'] = "one"
dict[2] = 2
dict[3] = "three"

print (dict)			# 打印dictionary
print (dict[2]) 		# 打印key为2的值
print (dict["one"])		# 打印key为one的值
print (dict.keys())		# 打印所有key
print (dict.values())	# 打印所有value

#------------------
print ("------------")
print ("类型转换：")
print ("int(x [,base])")
print (int("11", 2))
print (int(12.4))
# ValueError: invalid literal for int() with base 2: '11.2'
# print (int("11.2", 2))
