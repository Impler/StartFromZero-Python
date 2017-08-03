#!/bin/bash/python3

class A:
	__num = 0

	def __init__(self, num):
		self.__num = num

    ## toString
	def __str__(self):
		return 'A(%d)' %(self.__num)

	def getNum(self):
		return self.__num

	def __add__(self, other):
		if isinstance(other, A):
			self.__num += other.getNum()

a1 = A(2)
a2 = A(3)
a1 + 3
## 输出A(2)
print(a1)
a1 + a2
## 输出A(5)
print(a1)