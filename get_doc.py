import numpy as np

data1 = np.genfromtxt("save_data1.csv", delimiter=",", names=["id", "value1", "value2", "value3"])
print(data1)
data2 = np.genfromtxt("save_data2.csv", delimiter=",", names=["id", "value1", "value2", "value3"])
print(data2)
##调用genfromtxt()函数时，由于csv格式文件第一行为属性表头，所以必须要用names指定数组的名称(属性)，否则会默认从数组的第二行开始读取输出。
##genfromtxt()函数可以识别空白的数值，填充为nan值。
