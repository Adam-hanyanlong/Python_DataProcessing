import pandas as pd
import numpy as np

a = pd.Series([1, 2, 3, 4])
print(a)
print("_______________")
b = np.log(a)  # 使用numpy库的运算函数时要把Series实例当作参数传入函数
print(b)
# Series对象的组成元素，对元素进行重复判断等
serd = pd.Series([0, 1, 1, 3, 3, 4], index=["a", "b", "c", "d", "e", "f"])
print(serd)
print(serd.unique())
print(serd.value_counts())  # 输出各元素的出现次数
print(serd.isin([1]))  # 判断各元素值是否是1，输出bool值
print("—————————NaN——————————")
# 当数据不存在时，返回的结果会是Not a Number(非数值)，也称缺失项。
# 有两个函数可以判断并输出bool——>notnull()或isnull()
s2 = pd.Series([5, 3, np.NaN, 9], index=["5", "3", "NaN", "9"])
print("不是NaN吗？：\n{}".format(s2.notnull()))
print("是NaN吗？：\n{}".format(s2.isnull()))
print("——————Series用作字典——————")
ceshi_dict = {"姓名": "Adam", "性别": "男", "年龄": "22岁"}
print(pd.Series(ceshi_dict))
# 用Serie()函数也可以单独指定索引，键值自动进行匹配，pandas会控制字典的键和数组索引标签之间的相关性。
# 如果遇到缺失处会自动添加NaN值。
data_xinxi = ["年龄","姓名","性别","爱好"]
c = pd.Series(ceshi_dict,index=data_xinxi)
print(c)
