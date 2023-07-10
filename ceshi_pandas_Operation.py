import pandas as pd
import numpy as np

# 灵活算术运算
# 加法add()  减法sub()  除法div()  乘法mul()等
# 详情请关注网站 https://www.runoob.com/python3/python-operator.html
# DataFrame和Series对象之间也可以进行运算
frame = pd.DataFrame(np.arange(9).reshape(3, 3), columns=["a", "b", "c"])
print(frame)
ser = pd.Series(np.arange(1, 4), index=["a", "b", "c"])
print(ser)
print(frame - ser)
ser1 = pd.Series(np.arange(1, 5), index=["a", "b", "c", "d"])
print(frame - ser1)
# 当一个索引项只出现在其中一个数据结构中时，运算结果中会为该索引生成一列，该列的元素都为NaN值
print("_________________________")
# 操作元素的函数，nfunc(通用函数)，例如sqrt()根号函数
print(frame)
print(np.sqrt(frame))


# 除了使用通用函数，也可以自定义函数
# 例如：
def my_fuc(x):
    return x.max() - x.min()


# 计算的方式是列(直接调用的函数)
print("调用函数的第一种方式：\n{}".format(my_fuc(frame)))  # 将frame作为值传入自定义函数进行计算
# 计算的方式是行(使用apply()函数，apply(函数,axis = 0或1)，0是对列进行计算，1是对行进行计算)
print("调用函数的第二种方式：\n{}".format(frame.apply(my_fuc, axis=1)))  # 针对frame对象使用函数apply()


# apply()函数也可以执行很多次，返回多个数值
# 定义一个新函数
def my_fuc1(x):
    return pd.Series([x.max(), x.min()], index=["max", "min"])


print(frame)
print(frame.apply(my_fuc1, axis=0))  # 对列操作
print(frame.apply(my_fuc1, axis=1))  # 对行操作

print("______________________")
# 统计函数（求和  求平均） 两种方式
print(frame)
frame_sum = frame.sum(axis=0)  # 第一种  # axis=1默认跨列计算
print(frame_sum)
frame_sum1 = frame.apply(sum, axis=1)  # 第二种
print(frame_sum1)
frame_mean = frame.mean()  # 第一种
print(frame_mean)
frame_mean1 = frame.mean(axis=1)  # 第二种
print(frame_mean1)
# 排序函数 sort_index()函数
ser2 = pd.Series(np.arange(0, 4), index=["red", "green", "blue", "apple"])
print(ser2)
print("_________排序后__________")
# 若index为字母，则按照首字母顺序进行排序
ser_sort = ser2.sort_index()
print(ser_sort)
print("________________________")
ser3 = pd.Series(["你好", "hello world", "我是adam", "!!!!"], index=[5, 3, 2, 9])
print(ser3)
ser3_sort = ser3.sort_index()
print(ser3_sort)
# 也可以进行降序操作，需要添加ascending=False参数
print("________降序操作_________")
ser3_sort_ascending = ser3.sort_index(ascending=False)
print(ser3_sort_ascending)
# 针对DataFrame对象也能按照需求对行或列进行排序，只需要添加参数axis
print("_______________________")
frame_sort = pd.DataFrame(np.arange(9).reshape(3, 3),
                          index=[5, 2, 8], columns=["xiaomi", "apple", "huawei"])
print(frame_sort)
frame_sort_index = frame_sort.sort_index()  # 对DataFrame对象的index行进行排序
print(frame_sort_index)
frame_sort_columns = frame_sort_index.sort_index(axis=1)  # 对DataFrame对象的columns列进行排序
print(frame_sort_columns)
print("__________对数据内部元素进行排序(有优先级的排序)_____________")
frame_sort_new = pd.DataFrame({"one": [5, 8, 9], "two": [2, 1, 7], "three": [6, 9, 4]})
print(frame_sort_new)
frame_sort_new = frame_sort_new.sort_values(by=["one", "two", "three"])
print(frame_sort_new)
# 相关性和协方差的计算(两个series对象之间)
print("_______________________________")
seq = pd.Series([3, 4, 3, 4, 5, 4, 3, 2],
                index=["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"])
seq2 = pd.Series([1, 2, 3, 4, 4, 3, 2, 1],
                 index=["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"])
print("seq和seq2之间的相关性为:{}".format(seq.corr(seq2)))
print("seq和seq2之间的协方差为:{}".format(seq.cov(seq2)))
# 对DataFrame对象计算相关性和协方差
print("______________________________")
frame2 = pd.DataFrame([[5, 6, 2, 8], [7, 5, 1, 2], [4, 9, 6, 3], [1, 4, 7, 8]],
                      index=["a", "b", "c", "d"],
                      columns=["e", "f", "g", "h"])
print(frame2)
frame2_corr = frame2.corr()
frame2_cov = frame2.cov()
print("frame2的各元素之间相关性为：\n{}".format(frame2_corr))
print("frame2的各元素之间协方差为：\n{}".format(frame2_cov))
print("_____________________")
# 使用corrwith()方法可以计算DataFrame对象的列或行两两之间的相关性
# 为元素赋NaN值时可用np.nan的方法，同时也有过滤NaN值的函数
print(frame)
frame3 = frame.copy()
frame3["d"] = np.NaN
print(frame3)
# 在对DataFrame对象进行过滤Nan值时比较麻烦，只要某行某列有一个Nan值，整行整列就会被过滤，因此要在dropna中加入how值
print(frame3.dropna(how="all", axis=1))  # 不添加axis值默认对行进行过滤

