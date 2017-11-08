#!/bin/bash/python3
# -*- encoding: UTF-8 -*-

import re

# match 123
print(re.fullmatch('\d+', '123'))
# None
print(re.fullmatch('\d+', '123d'))



