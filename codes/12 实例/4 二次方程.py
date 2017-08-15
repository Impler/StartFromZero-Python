import cmath

print("求解二次方程式 ax^2 + bx + c = 0")
a = float(input("输入a："))
b = float(input("输入b："))
c = float(input("输入c："))

d = (b**2) - (4*a*c)

r1 = (-b + cmath.sqrt(d)) / 2
r2 = (-b - cmath.sqrt(d)) / 2

print("{0}x^2 + {1}x + {2} = 0的结果为{3},{4}".format(a, b, c, r1, r2))