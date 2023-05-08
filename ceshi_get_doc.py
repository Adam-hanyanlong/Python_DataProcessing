import numpy as np

data1 = np.genfromtxt("save_data1.csv", delimiter=",", names=["id", "value1", "value2", "value3"])
print(data1)
data2 = np.genfromtxt("save_data2.csv", delimiter=",", names=["id", "value1", "value2", "value3"])
print(data2)
