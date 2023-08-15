import numpy as np

a = np.arange(0, 9).reshape(3, 3)
b = np.arange(9, 18).reshape(3, 3)
print("———————————打印a数组—————————")
print(a)
print("———————————打印b数组—————————")
print(b)
print("————————————ab矩阵积运算(dot函数)————————")
print(np.dot(a, b))  # 矩阵积运算
print("————————————ba矩阵积运算————————")
print(np.dot(b, a))  # 矩阵积运算
print("———————————比较大小生成布尔数组————")
print(a > 5)
print("——————————比较大小生成新数组覆盖原数组————")
print(a[a > 5])
print("————————————矩阵的转置(transpose函数)————————")
print(a.transpose())  # 矩阵转置
print("————————————连接数组—————————————————")

# 连接数组（运用栈的函数）
print("———————将a和b两个函数通过垂直入栈来连接(vstack函数)—————————")
print(np.vstack((a, b)))  # vstack将a和b两个函数通过垂直入栈来连接
print("—————— 将a和b两个函数通过水平入栈来连接(hstack函数)—————————")
print(np.hstack((a, b)))  # hstack将a和b两个函数通过水平入栈来连接
print("—————————对一维数组操作压入栈中，按照行(row)组成新的数组(row_stack函数)——————")
print(np.row_stack((a, b)))
print("—————————对一维数组操作压入栈中，按照列(column)组成新的数组——————")
print(np.column_stack((a, b)))
# 分割数组
print("———————水平切分数组(hsplit函数)—————————")
A = np.arange(0, 12).reshape(3, 4)
[a1, a2] = np.hsplit(A, 2)
print("A:{}".format(A))
print("a1:{}".format(a1))
print("a2:{}".format(a2))
print("———————垂直切分数组(vsplit函数)—————————")
B = np.arange(0, 8).reshape(2, 4)
[b1, b2] = np.vsplit(B, 2)
print("B:{}".format(B))
print("b1:{}".format(b1))
print("b2:{}".format(b2))
print("———————按需求切分数组(split函数)—————————")
print(A)
[e, f, g] = np.split(A, [1, 3], axis=1)  # axis = 1为按列切割，= 0为按行切割  #其中[2,3]，表示序号为2的列之前和序号为3之前为分割线
print(e)
print(f)
print(g)
print("——————赋值运算不会为数组和数组任何元素创建副本，只是一种调用方式——————")
a = np.arange(0,4)
print(a)
b = a #将a赋值给b
print("把数组a赋值给数组b为：{}".format(b))
a[1] = 8 #对a[1]进行数值的改变
print("改变后的a：{}".format(a))
print("数组b为：{}".format(b))
print("##此时改变数组a的值，数组b的值也会改变。说明b只是调用a，而不是产生了a的副本")
c = a.copy()
print("创建数组a的副本c为：{}".format(c))
a[1] = 16
print("改变后的a{}".format(a))
print("数组c为：{}".format(c))
