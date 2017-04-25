# StartFromZero-Python
# Python
## 1 标识符
- 以英文字母或`_`开头
- 可包含字母、数字和下划线
- 不可包含标点符号：@、$、%
- 大小写敏感

### 1.1 常见标识符规则
- 类名：大写英文字母开头，后面使用小写字母
- 使用单个下划线开头的标识符表示private成员
- 使用两个下划线开头的标识符strongly表示private成员
- 使用两个下划线结尾的标识符表示语言特定的特殊名称

### 1.2 保留字

||||
|:-:|:-:|:-:|
|and|exec|not|
|as|finally|or|
|assert|for|pass|
|break|from|print|
|class|global|raise|
|continue|if|return|
|def|import|try|
|del|in|while|
|elif|is|with|
|else|lambda|yield|
|except|||

### 1.3 代码块
Python使用缩进组织代码块而不是{}，同一代码块的代码缩进量必须一致。  

### 1.4 多行语句
Python的语句遇到换行时结束。如果一条语句需要换行，需要使用换行连接符`\`。如：  
```python
total = item_one + \
		item_two + \
		item_three
```
如果语句中包含[]、{}、()，换行时则不需要使用'\'  

### 1.5 引号
在Python中单引号('')、双引号("")、三引号("""""")均可以表示字符串，一般三引号用于需要换行的字符串  

### 1.6 注释
- 单行注释以'#'开头  
- 多行注释使用三个单引号(''')或三个双引号(""")将注释括起来  

```python
# 这是单行注释
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
'''
"""
这是多行注释，用三个单引号
这是多行注释，用三个单引号 
这是多行注释，用三个单引号
"""
```

### 1.7 分号
多个语句同在一行时，使用分号分隔

### 1.8 suite
一组独立的语句组成的代码块成为suite，例如if、while、def等语句。suite的首行以关键字开头，行尾以':'结束，下面紧跟着该suite下的代码块
```python
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite
```

## 2 数据类型
在定义Python变量时，不需要指定其数据类型，数据类型是根据赋值的数据类型确定的。如：  
```python
counter = 100  # 整型
miles = 100.0  # 浮点型
name = "TOM"   # 字符型 
```
Python的赋值语句很随性，`a = b = c = 1`、`a, b, c = 1, 2, "tom"`都是合法的。  
Python主要包含5种数据类型，分别是：Numbers、String、List、Tuple、Dictionary。  

### 2.1 Numbers类型
Python的包含3种数字类型：
- int：整型，可表示长整型
- float：浮点型
- complex：复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

使用`del`语句删除变量的引用：  
```python
del counter  # 删除单个变量引用
del a, b, c  # 删除多个变量引用
```

### 2.2 String类型
被''、""、""""""包裹的值为String类型。
- String类型可以通过`[下标]`获取每个位置上的字符，也可以通过`[start:end]`获取串的子串。
- 使用`*`重复字符串
- 使用`+`拼接字符串

```python
str = "hello world"

print (str)                     # 打印字符串
print (str[0])					# 打印第一个字符 						
print (str[2:4])				# 打印第3到第5个字符，左闭右开区间[2,4)
print (str[2:])					# 打印第三个及以后的字符	
print (str * 3)					# 打印三遍
print (str + ' hello python')   # 拼接
```
### 2.3 List类型
用`[]`括起来的，包含多个值、彼此之间逗号分隔的数据类型为List类型。如：`['a', 1, 'c', 2, 4]`，List中的子元素数据类型不必完全一致。List变量访问方式同String类型：  
```python
list = ['a', 1, 'c', 2, 4]
alist = ['b', 'c']
			
print (list)					# 打印list
print (list[0])					# 打印第一个元素
print (list[1:7])				# 打印第二到八个元素
print (list[2:])				# 从第三个元素开始打印
print (list * 2)				# 重复打印两遍
print (list + alist)			# 两个集合拼接
```

### 2.4 Tuple类型
Tuple类型与List类型相似，区别在于形式上，tuple类型使用`()`包围，另外，tuple相当于不可改变的list，只能当做常量使用，其值不能更改。
```python
tuple = ('a', 1, 'c', 2, 4)
atuple = ('b', 'c')

print (tuple)					# 打印tuple
print (tuple[0])				# 打印第一个元素
print (tuple[1:7])				# 打印第二到八个元素
print (tuple[2:])				# 从第三个元素开始打印
print (tuple * 2)				# 重复打印两遍
print (tuple + atuple)			# 两个tuple拼接

# list的元素可以随意改变
print ("原list：")
print (list)
list[0] = 2
print ("修改后list：")
print (list)

# tuple的元素不可改变
# TypeError: 'tuple' object does not support item assignment
# tuple[0] = 2
```

### 2.5 Dictionary类型
Dictionary类型类似于Java中的Map类型，一种key-value的表现形式。key和value可以是任何类型，但是一般来说，使用数字或字符型作为key。Dictionary类型使用`{}`包裹。  
```python
print ("Dictionary类型：")
dict = {"k1": "v1", "k2":1}
dict['one'] = "one"
dict[2] = 2
dict[3] = "three"

print (dict)			# 打印dictionary
print (dict[2]) 		# 打印key为2的值
print (dict["one"])		# 打印key为one的值
print (dict.keys())		# 打印所有key
print (dict.values())	# 打印所有value
```
###2.6 Set类型
set是一个无序不重复元素的序列。  
基本功能是进行成员关系测试和删除重复元素。  
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。  
``` python
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

```

### 2.7 类型转换

|方法|描述|实例
|:--:|:--|:--|
|int(x [,base])|把数字x转成整数（直接舍去小数部分），或是把字符x转成整数，base指定当前数字表示的进制||
|float(x)|将x转换到一个浮点数||
|complex(real [,imag])|创建一个复数||
|str(x)|将对象 x 转换为字符串||
|repr(x)|将对象 x 转换为表达式字符串||
|eval(str)|用来计算在字符串中的有效Python表达式,并返回一个对象||
|tuple(s)|将序列 s 转换为一个元组||
|list(s)|将序列 s 转换为一个元组||
|set(s)|转换为可变集合||
|dict(d)|创建一个字典。d 必须是一个序列 (key,value)元组。||
|frozenset(s)|转换为不可变集合||
|chr(x)|将一个整数转换为一个字符||
|unichr(x)|将一个整数转换为Unicode字符||
|ord(x)|将一个字符转换为它的整数值||
|hex(x)|将一个整数转换为一个十六进制字符串||
|oct(x)|将一个整数转换为一个八进制字符串||

## 3 操作符
Python包含所有常见的基本操作符，也新增了一些操作符。  
- 算术运算符：+、-、*、/、%、**(指数)、//（整除商）
例如：  
```python
print ("2**2=",2**2) 		# 4
print ("19//4=", 19//4) 	# 4
print ("-12//5=", -12//5) 	# -3
print ("12//-5=", 12//-5) 	# -3
```
- 关系运算符：==、!=、>、>=、<、<=
- 赋值运算符：=、+=、-=、*=、/=、%=、**=、//=
- 逻辑运算符：and、or、not（小写）
- 位运算符：&、|、^、~、<<、>>
- 成员运算符：in、not in （strings，lists，tuples）
例如：
```python
str = "abcdef"
print ("'d' in", str, "=", "d" in str)		# True
print ("'g' in", str, "=", "g" in str)		# False
```
- id运算符：is、is not（比较对象的地址是否一样，同id()方法）
例如：  
```python
s1 = "a"
s2 = "a"
s3 = "b"
print ("id(s1) =", id(s1))
print ("id(s2) =", id(s2))
print ("id(s3) =", id(s3))
print ("s1 is s2 =", s1 is s2)		#True
print ("s1 is s3 =", s1 is s3)		#False
```

### 3.1 操作符优先级

|操作符|优先级|
|:-:|:-:|
|** |1|
|~, +, -, |2|
|*, /, %, //, |3|
|+, -, |4|
|>>, <<, |5|
|& |6|
|^, \|, |7|
|<=, <, >, >= |8|
|<, >, ==, != |9|
|=, %=, /=, //=, -=, +=, *=, **=, |10|
|is, is not |11|
|in, not in |12|
|not, or, and |13|

## 4 if 语句
在Python中，非0或非空的表达式视为TRUE, 0或空值的表达式视为FALSE。  
### 4.1 if语句
```python
if expression:
   statement(s)
```
### 4.2 if-else语句
```python
if expression:
   statement(s)
else:
   statement(s)
```
#### 4.2.1 if-elif-else语句
```python
if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
```
### 4.3 if 嵌套
```python
if expression1:
   statement(s)
   if expression2:
      statement(s)
   elif expression3:
      statement(s)
   else
      statement(s)
elif expression4:
   statement(s)
else:
   statement(s)
```

## 5 循环语句
### 5.1 while 循环
```python
while expression:
   statement(s)
```
此外，while可以搭配else使用，当循环条件不满足时调用：  
```python
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")
```

### 5.2 for 循环
for循环用于迭代集合、序列等对象。  
```python
for iterating_var in sequence:
   statements(s)
```
python内置方法`range()`，用于迭代数字，可用于循环中：  
```python
for var in list(range(5)):
   print (var)
```
同样，for也可以搭配else使用：  
```python
for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')
```

同其他语言，python同样支持在循环中使用break结束循环、continue跳过当次循环。  
此外python在循环中新增`pass`语句，不执行任何操作，只起到占位作用:  
```python
for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")
```
### 5.3 Iterator对象
`iter()`方法用于创建字符串、List、Tuple对象的Iterator对象，`next()`方法返回Iterator对象的迭代结果。  
```python
list = [1,2,3,4]
# 创建List的迭代对象
it = iter(list) 
# 打印迭代对象的下一个值
print (next(it))
# 迭代器对象可用在循环中
# for 循环
for x in it:
   print (x, end=" ")

# while循环
while True:
   try:
      print (next(it))
   except StopIteration:
      sys.exit()

```
### 5.5 Generator 对象
generator 是指使用`yield`方法使一个方法产生一个可迭代的序列。  
当一个generator被调用时，并不是直接返回方法执行后的结果，而是先返回一个generator对象。当使用`next()`方法调用generator时，方法才开始执行，并在`yield`方法处暂停，返回此时的结果；待到下一次`next()`调用过来，方法从上一步`yield`暂停处，继续执行，直到遇到下一个`yield`，以此类推。  
```python
# 定义一个generator方法(内部使用了yield)
def fibonacci(n): 
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n): 
         return
      yield a
      a, b = b, a + b
      counter += 1
# f为一个generator对象，而非方法执行返回的结果
f = fibonacci(5) 

# 迭代这个generator对象
while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
```
