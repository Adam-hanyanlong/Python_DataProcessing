import numpy as np
import csv

data1 = np.array([(1, 123, 1.4, 23), (2, 110, 0.5, 18), (3, 164, 2.1, 19)],
                 dtype=[("id", "i1"), ("value1", "i4"), ("value2", "f2"), ("value3", "i2")])
print(data1)
print(data1.dtype)
print(data1["id"])
np.savetxt("save_data1.csv", data1, fmt="%r", delimiter=",")
