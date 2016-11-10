#!/usr/bin/python3

print ("--------------")
print ("算术运算符")
print ("2**2=",2**2) 		# 4
print ("19//4=", 19//4) 	# 4
print ("-12//5=", -12//5) 	# -3
print ("12//-5=", 12//-5) 	# -3

print ("--------------")
print ("成员操作符")
str = "abcdef"
print ("'d' in", str, "=", "d" in str)		# True
print ("'g' in", str, "=", "g" in str)		# False

print ("--------------")
print ("ID操作符")
s1 = "a"
s2 = "a"
s3 = "b"
print ("id(s1) =", id(s1))
print ("id(s2) =", id(s2))
print ("id(s3) =", id(s3))
print ("s1 is s2 =", s1 is s2)		#True
print ("s1 is s3 =", s1 is s3)		#False