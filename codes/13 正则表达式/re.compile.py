#!/bin/bash/python3
# -*- encoding: UTF-8 -*-

import re

regexObj = re.compile('\d+')
# 输出 <class '_sre.SRE_Pattern'>
print(type(regexObj))
# match 12345, 相当于re.match('\d+', '12345')
print(regexObj.match('12345'))
