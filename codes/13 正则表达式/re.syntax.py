#!/bin/bash/python3

# -*- encoding: UTF-8 -*-

import re

# pattern .
print("==========pattern .==========")
# match a
print(re.match('.', 'abc'))
# None
print(re.match('.', '\n'))
# match \n
print(re.match('.', '\n', re.DOTALL))

# pattern 
print("\n==========pattern ^==========")
# match d
print(re.match('^d', 'def'))
# match None
print(re.match('[^abc]', 'b'))
# match d
print(re.match('[^abc]', 'd'))

# pattern $
print("\n==========pattern $==========")
# match abc
print(re.match('.*c$', 'abc'))
# None
print(re.match('.*c$', 'ab'))
# None
print(re.match('foo\d$', 'foo1\nfoo2'))
# match foo1
print(re.match('foo\d$', 'foo1\nfoo2\n', re.MULTILINE))

# pattern *
print("\n==========pattern *==========")
# match abc
print(re.match('.*', 'abc'))
# match a
print(re.match('a.*', 'a'))

# pattern +
print("\n==========pattern +==========")
# match abc
print(re.match('.+', 'abc'))
# None
print(re.match('a.+', 'a'))

# pattern ?
print("\n==========pattern ?==========")
# match a
print(re.match('a?', 'ab'))
# match ''
print(re.match('a?', 'bc'))
# match a
print(re.match('a.?', 'a'))

# pattern *?、+?、??
print("\n==========pattern *?、+?、??==========")
# match <a>b<c>
print(re.match('<.*>', '<a>b<c>'))
# match <a>
print(re.match('<.*?>', '<a>b<c>'))

# pattern {m}、{m,}、{m, n}
print("\n==========pattern {m}、{m,}、{m, n}==========")
# None
print(re.match('a{3}', 'aa'))
# match aaa
print(re.match('a{3}', 'aaa'))
# match aaa
print(re.match('a{3,}', 'aaa'))
# match aaaa
print(re.match('a{3,}', 'aaaa'))
# match aa
print(re.match('a{1,3}', 'aa'))
# match aaa
print(re.match('a{1,3}', 'aaaa'))

# pattern {m,}?、{m, n}?
print("\n==========pattern {m,}?、{m, n}?==========")
# match aa
print(re.match('a{2,3}?', 'aaa'))
# match aa
print(re.match('a{2,}?', 'aaa'))

# pattern []
print("\n==========pattern []==========")
# match a
print(re.match('[abc]', 'abc'))
# match b
print(re.match('[a-c]', 'b'))
# match *
print(re.match('[+*]', '*'))
# match d
print(re.match('[^abc]', 'd'))

# pattern |
print("\n==========pattern |==========")
# match ab
print(re.match('ab|cd', 'abc'))
# None
print(re.match('a|bcd', 'bc'))

# pattern ()
print("\n==========pattern ()==========")
# groups ('12',)
print(re.match('abc(\d+)cd', 'abc12cd').groups())

# pattern (?...)
print("\n==========pattern (?...)==========")
# match A
print(re.match('(?i)a', 'A'))

# pattern (?:...)
print("\n==========pattern (?:...)==========")
# match body
print(re.match('bo(?:y|dy)', 'body'))

# pattern (?P<name>pattern)
print("\n==========pattern (?P<name>pattern)==========")
# 匹配双引号字符串，同(").*?"
# match "abc"
print(re.match('(?P<quote>").*?(?P=quote)', '"abc"'))
# group quote = "
print(re.match('(?P<quote>").*?(?P=quote)', '"abc"').groups())


# pattern (?=pattern)
print("\n==========pattern (?=pattern)==========")
# match Windows
print(re.match('Windows(?=98|2000|xp)', 'Windows2000'))

# pattern (?!pattern)
print("\n==========pattern (?!pattern)==========")
# match Windows
print(re.match('Windows(?!98|2000|xp)', 'Windows 10'))

# pattern (?<=pattern)
print("\n==========pattern (?<=pattern)==========")
# match  boy
print(re.match('(?<=hate|love)abc', 'hateabc'))
