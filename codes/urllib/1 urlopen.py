#!/bin/bash/python3
import urllib.request 
response = urllib.request.urlopen("http://www.baidu.com").read()
print(response)