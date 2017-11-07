#!/bin/bash/python3
# -*- encoding:utf-8 -*-

import re
phone1 = "(+86)1234-1234-123"
phone2 = "4321-4321-321"
phone3 = "+8612345678901"
phone4 = "34567890123#这是一个电话号码"
pattern = '[(]?\+86[)]?|-|#.*'
# 输出 12341234123
print(re.sub(pattern, "", phone1))
# 输出 1234-1234-123
print(re.sub(pattern, "", phone1, 1))
# 输出 4321*4321*321
print(re.sub(pattern, "*", phone2))
# 输出 12345678901
print(re.sub(pattern, "", phone3))
# 输出 34567890123
print(re.sub(pattern, "", phone4))

print(re.search("foo.$", "foo1\nfoo2\n", re.MULTILINE))
print(re.search("$", "foo1\n", re.MULTILINE).group())
print(re.search("ab*", "a").group())