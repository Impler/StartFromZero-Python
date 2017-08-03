#! /bin/bash/python3

class A:
	def __init__(self):
		print("enter A")
		print("leave A")

	def print(self):
		print("A")


class B(A):
	def __init__(self):
		print("enter B")
		A.__init__(self)
		print("leave B")
class C(A):
	def __init__(self):
		print("enter C")
		A.__init__(self)
		print("leave C")


class D(B, C):
	def __init__(self):
		print("enter D")
		B.__init__(self)
		C.__init__(self)
		print("leave D")

	# ������д
	def print(self):
		print("D")

d = D()
d.print()

## �����
## enter D
## enter B
## enter A
## leave A
## leave B
## enter C
## enter A
## leave A
## leave C
## leave D
## D