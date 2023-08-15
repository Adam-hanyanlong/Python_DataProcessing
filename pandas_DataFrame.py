import pandas as pd
import numpy as np

# 定义DataFrame的方法  先定义好数组(numpy的方式)，然后定义index和column参数
frame = pd.DataFrame(np.arange(0, 16).reshape(4, 4),
                     index=["0", "1", "2", "3"], columns=["a", "b", "c", "d"])
print(frame)
print("________________")
# 对frame进行切片处理
frame1 = frame[1:3]
print(frame1)
print("________________")
print(frame[1:3])
print("________________")
# 选取一列
print(frame["a"])  # 或frame.a
# 选取多列
print(frame[["a", "c"]])
# 一定要注意区分frame[]和frame[[]],有以下解释：
# 当要使用切片操作时[1:3]代表的是一个范围。当要选取多个属性目标时[["a","c"]],中间代表一个数组，数组的值为a和c。
# 不能直接用frame["a","c"]来提取列值！！
print("_________________")
print(frame)
# 新增一列
frame["new"] = 8
print(frame)
# 也可以通过Serie实例新增数据
ser = np.arange(0, 4)
frame["new1"] = ser
print(frame)
# 修改单个元素的方法
frame2 = pd.DataFrame(np.arange(0, 4).reshape(2, 2), index=["1", "2"], columns=["red", "blue"])
print(frame2)
frame2["red"][1] = 8
print(frame2)
# 删除一列用 del函数，之后还有drop()函数
del frame["new"]
del frame["new1"]
print(frame)
# 修改frame的单个元素值。？？？？这里有疑问
# ？？？？？在对添加元素后的frame进行修改单个元素时会出现报错，怀疑是调用问题，而不是新的frame
frame["a"][2] = 9
print(frame)
print("______以下为测试疑问问题的代码部分______")
# 对frame增加一列
frame["new"] = 9
print(frame)
frame.loc["2", "new"] = 11
print(frame)
# frame["new"][2] = 2  #！！！！这里会报错
# print(frame)
# 尝试在增加一列后生成一个新的行列式
# frame3 = frame.copy()
# print(frame3)
# frame3["new"]["2"] = 5 # 同样会报错！
# print(frame3)
# # https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
# # https://blog.csdn.net/zhaoyuanh/article/details/126720017
# # 在这个网站上找到了答案
# frame3.loc["2","a"] = 11
# print(frame3)
# 最后发现不是副本的问题，而是链式索引的赋值问题，连续使用链式索引会产生不可预测的后果，所以会警告报错。
# 什么是链式索引？就是对DataFrame连续地使用[]进行索引，底层行为表现为连续使用__getitem__操作，这是线性依次的操作，而不是整体地对最初地DataFrame进行操作。
# 所以最好不使用链式索引，如果想对pandas对象设置值时，用loc["index","column"]方法即可!!记得加双引号。


print("__________元素的所属关系___________")
# 用isin()实例判断需求值是否属于DateFrame对象
print(frame.isin([9]))  # 得到了一个只包含bool值的DataFrame对象
print(frame[frame.isin([9])])  # 得到一个新的DateFrame，只包含满足条件的元素
# 筛选元素
print(frame[frame > 5])
# index对象
print(frame)
print(frame.idxmin())  # 返回index索引的最小值
print(frame.idxmax())  # 返回index索引的最大值
# 判断是否含有重复标签
print(frame)
print(frame.index.is_unique)
# 修改单个index的值
frame.rename(index={"2": "1"}, inplace=True)
print(frame)
print(frame.index.is_unique)
# 更换索引
# 先生成一个新的Series对象
ser_new = pd.Series(np.arange(5), index=[0, 2, 4, 5, 6])
print(ser_new)
ser_new = ser_new.reindex(range(5), method='bfill')  # reindex(value,method)函数可以插值,
# method=ffill表示插入的值和前一个的值相同，method=bfill表示插入的值和后一个的值相同。
print(ser_new)
# 更换索引的方法可以从series拓展到DataFrame,也可以添加新的行或列，pandas用NaN来填充数据结构中的缺失元素。
frame4 = pd.DataFrame(np.arange(16).reshape(4, 4), columns=["a", "b", "c", "new"])
frame4 = frame4.reindex(range(4), method='bfill', columns=["a", "b", "c", "new", "new1"])
print(frame4)
# 删除元素,drop()函数的应用
frame5 = pd.DataFrame(np.arange(0, 9).reshape(3, 3), index=[0, 1, 2], columns=["a", "b", "c"])
frame6 = pd.DataFrame(np.arange(0, 9).reshape(3, 3), index=[3, 4, 5], columns=["d", "e", "f"])
# 删除行元素
print("______frame5_____")
print(frame5)
frame5 = frame5.drop([0, 2], axis=0)  # axis = 0代表从横轴(行)删除元素
print("_____删除行后_______")
print(frame5)
# 删除列元素
print("______frame6_____")
print(frame6)
frame6 = frame6.drop(["d", "f"], axis=1)  # axis = 1代表从竖轴(列)删除元素
print("_____删除列后______")
print(frame6)
# 数据对齐
# pandas能够将两个数据结构的索引对齐，将索引项相同的数据进行运算
# 先定义两个DataFrame对象，让其进行运算
frame7 = pd.DataFrame(np.arange(16).reshape(4, 4), index=["red", "blue", "yellow", "white"],
                      columns=["ball", "pen", "pencil", "paper"])
frame8 = pd.DataFrame(np.arange(12).reshape(4, 3), index=["blue", "green", "white", "yellow"]
                      , columns=["mug", "pen", "ball"])
print(frame7)
print(frame8)
print(frame7 + frame8)
