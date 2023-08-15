import pandas as pd

# 读写CSV文件
csvframe = pd.read_csv("save_data1.csv", header=None)  # 或者用names = ["","",...,""]来定义表头
print(csvframe)

# 读写excel文件
# pandas 专门定义了几个函数来处理excel表格文件。I/O API函数中  to_excel()和read_excel()
# 其中read_excel()函数能够读取Excel2003(.xls)和Excel2007(.xlsx)两种类型的文件

