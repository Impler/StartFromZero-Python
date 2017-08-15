import cmath

num = input("请输入一个数字：")

sqrt_num = float(num) ** 0.5

print("{0}的平方根为：{1}".format(num, sqrt_num))
print("%s的平方根为：%.4f" %(num, sqrt_num))


# 使用负数数学模块
sqrt_num2 = cmath.sqrt(float(num))
print("{0}的平方根为：{1}".format(num, sqrt_num2))
print("{0}的平方根为：{1:0.3f}+{2:0.3f}j".format(num, sqrt_num2.real, sqrt_num2.imag))