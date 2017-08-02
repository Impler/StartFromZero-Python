#!/bin/bash/python3

# 使用print()打印数字的平方表
for x in range(1, 11):
	# rjust()用于右对齐输出，参数为位数；类似的还有左居中ljust(), 中间对其center()
	# end='  '为输出的每个值之间的间隔
	print(repr(x).rjust(4), repr(x*x).rjust(4), repr(x*x*x).rjust(4), end='  ')
	# 换行
	print()

print("-----------------------------")
# 使用str().format()打印数字的平方表
for x in range(1, 11):
	# {0:4d}：0表示第一个参数位置，4表示占4个字符，d表示参数为整型
	print('{0:4d} {1:4d} {2:4d}'.format(x, x*x , x*x*x))


print("-----------------------------")

print("{}和{}是好朋友".format("小红", "小明"))
# !a 代表ascii()
print("{!a}".format("你好"))
# !s 代表str()
print("{!s}".format("abcd"))
# !r 代表repr()
print("{!r}".format("abcd"))