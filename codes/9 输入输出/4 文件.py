#!/bin/bash/python3
# 以写入方式打开文件，文件不存在则创建，存在则覆盖
f = open("C:test.txt", "w")
# 写入
f.write("hello world")
f.write("\r")
f.write("你好")

f.close()