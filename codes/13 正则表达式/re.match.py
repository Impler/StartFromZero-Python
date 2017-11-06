#!/bin/bash/python3
## 指定文件编码
# -*- coding:utf-8 -*-

import re
matchObj = re.match("abc(\d+)d(.*)", "abc121d9b")
# 输出 matchObj ==> <_sre.SRE_Match object; span=(0, 9), match='abc121d9b'>
print("matchObj ==>", matchObj)
index = 0
groups = matchObj.groups()
# 输出 matchObj.groups() ==>  ('121', '9b')
print("matchObj.groups() ==> ", groups)
while index <= len(groups):
    # 输出 matchObj.group( 0 ) ==>  abc121d9b
    # 输出 matchObj.group( 1 ) ==>  121
    # 输出 matchObj.group( 2 ) ==>  9b
	print("matchObj.group(",index,") ==> ", matchObj.group(index))
	index = index + 1

# match从起始位置开始匹配，如果起始就不匹配则不再往下进行
unmatchObj = re.match("abc(\d+)d", "aaabc1d")
print(unmatchObj)
if unmatchObj is None:
	print("no match")