# StartFromZero-Python
# Python
Python优点：  
- 面向对象
- Python代码可维护性、可重用性高，软件质量好
- Python能够有效提高开发者效率
- Python程序可移植
- 丰富的标准库
- 灵活的集成机制

Python可以做些什么：  
- 系统编程
- 用户图形接口
- Internet脚本
- 组件集成
- 数据库编程
- 快速原型
- 数值计算和科学计算编程
- 游戏、图像、人工智能、XML、机器人等

Python程序可以分解成模块、语句、表达式以及对象：
- 程序由模块构成
- 模块包含语句
- 语句包含表达式
- 表达式建立并处理对象

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

### 2.4 Tuple（元组）类型
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

### 2.7 日期和时间
Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。  
时间间隔是以秒为单位的浮点小数。  
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。  
Python 的 time 模块下有很多函数可以转换常见日期格式。  
```python
import time;  # 引入time模块
ticks = time.time()
print("当前时间戳为:", ticks)
```

### 2.8 类型转换

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
### 5.4 Generator 对象
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

## 6 函数
### 6.1 定义函数
- 以`def`关键字开头，后接函数名和圆括号
- 入参放在圆括号中间
- 函数的第一行可以选择性的使用文档字符串--注释
- 函数内容以冒号起始，并且缩进
- return [表达式] 结束函数。不带表达式的return相当于返回none

```python
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]

# 方法定义
def printme(str):
	"打印传入的参数"
	print(str)
	return

# 方法调用
printme("hello world")
```

### 6.2 参数传递
在Python中，变量没有类型，仅仅是一个对象的引用（指针），只有对象是有类型的。  
在Python中，对象分为可更改对象和不可更改对象，像string，tuples和numbers 是不可更改对象，而 list，dict 则是可更改对象。  
- 当向方法中传递一个不可改变对象，相当于值传递，在方法内部对该对象副本的修改，不会影响对象本身
- 当向方法中传递一个可变对象时，相当于引用传递，任何修改都将直接作用于该对象上
``` python
a = 1
# 传递不可变对象
def changeme1(a):
	a = 2
	print("方法内a = ", a)
	return

# 输出
# 方法内a =  2
# 方法外a =  1
changeme1(a)
print("方法外a = ", a)

b = [1, 2, 3]
# 传递可变对象
def changeme2(b):
	b.append([4, 5, 6])
	print("方法内b = ", b)
	return
# 输出
# 方法内b =  [1, 2, 3, [4, 5, 6]]
# 方法外b =  [1, 2, 3, [4, 5, 6]]
changeme2(b)
print("方法外b = ", b)

```

### 6.3 实参
调用函数时可使用的正式参数类型:  
- 必备参数
- 关键字参数
- 默认参数
- 不定长参数

#### 6.3.1 必备参数
必备参数必须以正确的顺序传入函数。调用时的数量必须与声明时一致。  
```python
# 直接调用上面定义的printme函数
printme()
# 执行报错：
# Traceback (most recent call last):
# printme()
# TypeError: printme() missing 1 required positional argument: 'str'
```

#### 6.3.2 关键字参数
函数调用使用关键字参数来确定传入的参数值，参数顺序与生命顺序不必一致。  
```python
def printscore(name, score):
	print("学生：", name, "，分数：", score)
	return

stu = "小明"
mathScore = 99
# 输出 学生： 小明 ，分数： 99
printscore(stu, mathScore)
# 输出 学生： 小明 ，分数： 100
printscore(score=mathScore + 1, name=stu)
```

#### 6.3.3 缺省参数
函数调用时，缺省参数的值如果没有传入，则被任务是使用默认值。  
```python
def printAge(name, age = 10):
	print("学生：", name, "年龄：", age)
	return
# 输出 学生： 小明 年龄： 12
printAge("小明", 12)
# 输出 学生： 小红 年龄： 10
printAge("小红")
```

#### 6.3.4 不定长参数
如果函数定义时不能确定实际会传入多少个参数，则可以使用不定长参数。  
语法如下：  
```python
def functionname([formal_args,], *varName):
  function_suite
  return [expression]
```
加了（*）的变量名会存放所有未命名的变量参数。  
```python
def printFamily(father, *others):
	print("户主：", father)
	print("其他人：")
	for name in others:
		print(name)
# 输出
# 户主： father
# 其他人：
printFamily("father")

# 输出
# 户主： father
# 其他人：
# mather
# brother
printFamily("father", "mather", "brother")
```

### 6.4 匿名函数
Python使用lambda来创建匿名函数。  
- lambda只是一个表达式，函数体比def简单的多
- lambda的主体是一个表达式，而不是一个代码块。仅能封装有限的逻辑进去
- lambda函数拥有自己的命名空间，且不能访问自有参数列表外（包括全局命名空间里）的变量。
- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

语法如下：  
```python
lambda [arg1 [,arg2,.....argn]]:expression
```
示例：  
```python
sum = lambda n1, n2, n3: n1+n2+n3
# 输出6
print("求和：", sum(1, 2, 3))
```

### 6.5 全局变量和局部变量
定义在函数内部的变量拥有局部作用域。定义在函数外部的变量拥有全局作用域。  
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。同名的局部变量在局部作用域内会覆盖全局变量。  
```python
# 定义一个全局变量
total = 0
def add(num1, num2):
	# 定义一个重名的局部变量
	total = num1 + num2
	print("局部total = ", total)
	return total
# 输出 5
add(2, 3)
# 输出 0
print("全局total = ", total)
```
如果需要在局部作用域使用全局变量，则需要使用global关键字声明：  
```python
glbTotal = 0
def add1(num1, num2):
	# 定义一个重名的局部变量
	glbTotal = num1 + num2
	print("局部glbTotal = ", glbTotal)

	# 操作全局变量，需要使用global关键字声明，声明后的操作均作用于全局变量
	global glbTotal
	glbTotal = num1 + 1
	return glbTotal
# 输出 5
t = add1(2, 3)
# 输出 3
print("方法返回：", t)
# 输出 3
print("全局glbTotal = ", glbTotal)
```

如果需要修改嵌套作用域（外层非全局作用域）中的变量则需要使用nonlocal关键字声明：
```python
def outer():
	num = 1
	# 输出1
	print("outer num: ", num)
	def inner():
		num = 2
		# 输出2
		print("inner num: ", num)
		# 修改嵌套作用于变量
		nonlocal num
		num = 3

	inner()
	# 输出3
	print("outer num: ", num)
outer()
```

## 7 数据结构

### 7.1 列表

#### 7.1.1 列表中的常用方法

|方法|描述|
|:- |:- |
|list.append(x)|把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。|
|list.extend(L)|通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。|
|list.insert(i, x)|在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。|
|list.remove(x)|删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。|
|list.pop([i])|从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）|
|list.clear()|移除列表中的所有项，等于del a[:]。|
|list.index(x)|返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。|
|list.count(x)|返回 x 在列表中出现的次数。|
|list.sort()|对列表中的元素进行排序。|
|list.reverse()|倒排列表中的元素。|
|list.copy()|返回列表的浅复制，等于a[:]。|

#### 7.1.2 列表推导式
列表推导式提供了创建列表的简单途径。列表推导式是包含1个for语句和0个或多个for/if语句的子句组成的表达式。其形式为[表达式 for 变量 in 列表 if/for子句*]。  
```python
>>> list = [1,2,3,4]
>>> [3*x for x in list]
[3, 6, 9, 12]
>>> [[i, i*2] for i in list]
[[1, 2], [2, 4], [3, 6], [4, 8]]
>>> [x for x in list if x%2==0]
[2, 4]
```

#### 7.1.3 del语句
使用del语句可以从一个列表中依索引而不是值来删除元素。  
```python
>>> lists = [1,3,4,5,5,7]
## 删除第一个元素
>>> del lists[0]
>>> lists
[3, 4, 5, 5, 7]
## 删除第二到四个元素
>>> del lists[1:3]
>>> lists
[3, 5, 7]
## 清空列表
>>> del lists[:]
>>> lists
[]

## del也可以用来删除实体变量
>>> del lists
>>> lists
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'lists' is not defined
```

### 7.2 元组和序列
元组由若干逗号分隔的值组成，例如：
```python
>>> t = 1,2,2,3
>>> t
(1, 2, 2, 3)
>>> t[2]
2
>>> u = t, 4,5,6
>>> u
((1, 2, 2, 3), 4, 5, 6)
>>> p = t, u, (7,8,9)
>>> p
((1, 2, 2, 3), ((1, 2, 2, 3), 4, 5, 6), (7, 8, 9))
```

### 7.3 集合
集合是一个无序不重复元素的集合。可以用大括号`{}`创建，如果要创建一个空集合，必须使用`set()`而不是`{}`。后者则是用于创建一个空的字典。  
```python
>>> s = {1, 2, 2, 4}
>>> s
{1, 2, 4}
>>> 3 in s
False
>>> 4 in s
True

>>> a = set('abcd')
>>> a
{'c', 'a', 'b', 'd'}
>>> b = set('abef')
>>> b
{'a', 'b', 'e', 'f'}
## a中存在b中不存在
>>> a - b
{'c', 'd'}
## 在a或b中存在的字母
>>> a | b
{'c', 'd', 'e', 'b', 'f', 'a'}
## a、b中都存在的记录
>>> a & b
{'a', 'b'}
## 在a、b中的元素，但不同时存在于a、b中
>>> a ^ b
{'c', 'd', 'e', 'f'}
```

### 7.4 字典
一组键值对集合。使用大括号创建一个空的字典。  
```python
>>> dic = {'name':'tom', 'age': 12}
>>> dic
{'name': 'tom', 'age': 12}
>>> dic['name']
'tom'
>>> list(dic.keys())
['name', 'age']
>>> list(dic.values())
['tom', 12]
>>> 'name' in dic
True
>>> dic['age'] = 15
>>> dic
{'name': 'tom', 'age': 15}
```
构造函数 dict() 直接从键值对元组列表中构建字典:  
```python
>>> d = dict([('name', 'kitty'), ('age', 15)])
>>> d
{'name': 'kitty', 'age': 15}
```

### 7.5 遍历
字典的遍历可以使用`items()`方法同时获取键和对应的值：  
```python
>>> for k, v in d.items():
...   print(k, v)
...
name kitty
age 15
```

在序列遍历中，索引和对应位置的值，可以通过`enumerate()`获取：  
```python
>>> for i, v in enumerate(['abc', 'pad', 'apple']):
...     print(i, v)
...
0 abc
1 pad
2 apple
```

同时遍历两个或更多的序列，可以使用 `zip()`:  
```python
>>> a = ['a1', 'a2', 'a3']
>>> b = ['b1', 'b2', 'b3', 'b4']
>>> for p, q in zip(a, b):
...     print(p, q)
...
## 只会打印相同长度的内容
a1 b1
a2 b2
a3 b3
```

反向遍历一个序列，使用 `reversed()` 函数：  
```python
>>> for i in reversed([2, 4, 5, 6]):
...     print(i)
...
6
5
4
2
```

按顺序遍历一个序列，可以用`sorted()`方法返回一个排序的序列：  
```python
>>> for i in sorted([4, 1, 5, 3, 6]):
...     print(i)
...
1
3
4
5
6
```

## 8 模块
模块是一个包含所有定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。  

```python
#!/usr/bin/python3
## 文件名 m01.py
## 引入标准库中的sys.py模块
import sys
print('命令行参数如下：')
## sys.argv是一个包含命令行参数的列表
for i in sys.argv:
	print(i)
```
执行：  
```python
xxx>python m01.py v1 v2 v3
命令行参数如下：
m01.py
v1
v2
v3
```

### 8.1 import语句
在python源文件中使用import语句引入其他模块。  
语法为：`import module1[,module2[,... moduleN]]`  
一个模块只会被导入一次，不管执行多少次import。当使用import语句的时候，python通过搜索一系列目录来找到对应的文件。这些搜索路径存放在sys模块模块的path变量中。  
```python
>>> import sys
>>> sys.path
['', 'D:\\1_software\\Python\\python35.zip', 'D:\\1_software\\Python\\DLLs', 'D:
\\1_software\\Python\\lib', 'D:\\1_software\\Python', 'D:\\1_software\\Python\\l
ib\\site-packages']
```
sys.path输出的是一个列表，第一项是空串，代表当前目录或运行的脚本所在的目录。  
使用import引入模块后，通过`模块名.函数名`访问模块内函数:  
```python
#!/usr/bin/python3
## 文件名 fbi.py
## 打印n个斐波那契数列
def fib(n):
	i = 0
	a, b = 0, 1
	while i < n:
		print(a, end=' ')
		a, b = b, a+b
		i+=1
	print()

## 返回n个斐波那契数列
def fib2(n):
	i = 0
	result = []
	a, b = 0, 1
	while i < n:
		result.append(a)
		a, b = b, a+b
		i+=1

	return result
```
```python
>>> import fib
>>> fib.fib(4)
0 1 1 2
## 如果经常使用一个函数，可以把它赋给一个本地变量：
>>> myfib = fib.fib
>>> myfib(4)
0 1 1 2
```

### 8.2 from...import语句
from...import语句可以从模块中导入一个指定的部分到当前命名空间下：  
`from moduleName import name1[, name2[, ... nameN]]`
例如：  
```python
>>> from fib import fib, fib2
>>> fib(2)
0 1
>>> fib2(2)
[0, 1]
```
把一个模块的全部内容导入到当前的命名空间下使用：`from moduleName import *`，但是这种方式不建议使用，很可能覆盖当前命名空间下的定义。  

### 8.3 __name__属性
每个模块都有一个`__name__`属性，当其值为`__main__`时，标识该模块自身在运行，否则是被引入的。  

### 8.4 dir()函数
内置的`dir([moduleName])`函数可以找到模块内定义的所有名称。以一个字符串列表的形式返回。  

## 9 输入输出

### 9.1 输出
Python两种输出值的方式：表达式语句和`print()`函数。  
如果希望输出的形式更加多样，可以使用`str.format()`函数来格式化输出值。  
如果希望将输出的值转成字符串，可以使用`repr()`或`str()`函数实现。  
- str(): 返回一个用户易读的表达形式
- repr(): 产生一个解释器易读的表达形式，其参数可以使任意类型，且可以转译字符串中的特殊字符

#### 9.1.1 str.format()
Python String 类型常用的函数为：  
- ljust(num)：左居中输出，占num个字符
- rjust(num)：右居中输出，占num个字符
- center(num)：居中输出，占num个字符
- zfill(num)：左填充0，占num个字符

```python
print("{}和{}是好朋友".format("小红", "小明")) # 小红和小明是好朋友
# !a 代表ascii()
print("{!a}".format("你好"))	                 # '\u4f60\u597d'
# !s 代表str()
print("{!s}".format("abcd"))                 # abcd
# !r 代表repr()
print("{!r}".format("abcd"))                 # 'abcd'
```

### 9.2 输入

#### 9.2.1 读取键盘输入
```python
str = input("请输入：");
print("你输入的是：", str)

# 输出
请输入：hello world
你输入的是： hello world
```

### 9.3 读写文件
open() 将会返回一个 file 对象，基本语法格式如下:  
```python
open(filename, mode)
```
其中mode表示打开文件的模式。只读、写入、追加等。默认为只读（r）。所有取值如下：  

|模式|描述|
|:-|:-|
|r|以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。|
|rb|以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。|
|r+|打开一个文件用于读写。文件指针将会放在文件的开头。|
|rb+|以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。|
|w|打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。|
|wb|以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。|
|w+|打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。|
|wb+|以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。|
|a|打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。|
|ab|以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。|
|a+|打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。|
|ab+|以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。|

```python
#!/bin/bash/python3
# 以写入方式打开文件，文件不存在则创建，存在则覆盖
f = open("C:test.txt", "w")
# 写入
f.write("hello world")
f.write("\r")
f.write("你好")

f.close()
```

#### 9.3.1 文件对象的方法

- f.read([size])：可选参数size表示读取的字符数目，如果不传参数，则表示读取全部
- f.readline()：读取单独一行，换行符为"\n"。如果返回一个空字符串是表示读取到最后一行。
- f.readlines([size])：可选 参数size表示读取的行数，如果不传参数，则表示读取全部行。返回按行分割的数组。
- f.write()：写入文件，返回写入的字符数 
- f.tell()：返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
- f.seek(offset, from_what)：改变文件内字符的位置
	- offset：表示移动位数
	- form_what：表示开始位置，默认0
		- 0：从文件开头开始
		- 1：从当前位置开始
		- 2：从文件末尾开始
- f.close()：关闭文件并释放系统的资源





