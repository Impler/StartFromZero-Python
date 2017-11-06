#!/bin/bash/python3
# -*- coding:utf-8 -*-

import re

searchObj = re.search("abc(\d+)d(.*)", "abc121d9b")
# 输出 searchObj ==>  <_sre.SRE_Match object; span=(0, 9), match='abc121d9b'>
print("searchObj ==> ", searchObj)
groups = searchObj.groups()
# 输出 searchObj.groups() ==>  ('121', '9b')
print("searchObj.groups() ==> ", groups)
index = 0
while index <= len(groups):
	# 输出 searchObj.group( 0 ) ==>  abc121d9b
    # 输出 searchObj.group( 1 ) ==>  121
    # 输出 searchObj.group( 2 ) ==>  9b
    print("searchObj.group(", index, ") ==> ", searchObj.group(index))
    index = index + 1


unsearchObj = re.search("aba", "abc")
if unsearchObj is None:
	print("No match")

# 注意与re.match()的区别
searchObj = re.search("abc(\d+)d", "aaabc17d")
# 输出 <_sre.SRE_Match object; span=(2, 8), match='abc17d'>
print(searchObj)
# 输出 17
print(searchObj.group(1))