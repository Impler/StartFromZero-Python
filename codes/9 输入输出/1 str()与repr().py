#!/bin/bash/python3
s='Hello, World'
# str(s)= Hello, World
print("str(s)=", str(s))
# repr(s)= 'Hello, World'
print("repr(s)=", repr(s))

# repr() 函数可以转义字符串中的特殊字符
# repr() 的参数可以是Python的任何对象
s = 'Hello, World\n'
print("repr(s)=", repr(s))