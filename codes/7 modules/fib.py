#!/usr/bin/python3
## 文件名 fbi.py
## 打印n个斐波那契数列
def fib(n):
	i = 0
	a, b = 0, 1
	while i < n:
		print(a, end=' ')
		a, b = b, a+b
		i+=1
	print()

## 返回n个斐波那契数列
def fib2(n):
	i = 0
	result = []
	a, b = 0, 1
	while i < n:
		result.append(a)
		a, b = b, a+b
		i+=1

	return result