import numpy as np
import pandas as pd
import matplotlib.pylab as plt

# 绘制线性图 ——>plot()函数
# 更多代码方法详见 https://www.runoob.com/matplotlib/matplotlib-line.html
# 分为上下两个子图的图形
t = np.arange(0, 5, 0.1)
y1 = np.sin(2 * np.pi * t)
y2 = np.sin(2 * np.pi * t + np.pi / 2)
plt.subplot(211)  # subplot()参数为211，212为上下分布  参数为121，122为左右分布
plt.plot(t, y1, "b-.")
plt.subplot(212)
plt.plot(t, y2, "r--")
plt.show()

# 同一张图像上显示
plt.axis([0, 2.5, -1, 1])  # 定义x轴y轴的取值范围
plt.title("The student plot", fontsize=20, fontname="Times New Roman", color="red")  # 添加标题
plt.xlabel("Counting", fontsize=15, fontname=None, color="black")  # 添加x轴标签
plt.ylabel("Square values", fontsize=15, fontname=None, color="black")  # 添加y轴标签
# matplotlib整合了LaTeX表达式，支持在图标中插入数学表达式
# 将表达式内容置于两个$符号之间，可在文本中添加LaTeX表达式。
plt.text(1.05, 0.75, r"$y=sin(x)$", fontsize=20, bbox={'facecolor': 'white', 'alpha': 0.2})  # 添加的新标签
plt.text(1.05, 0.50, r"$y=cos(x)$", fontsize=20, bbox={'facecolor': 'white', 'alpha': 0.2})  # 添加的新标签
plt.grid(False)  # 添加网格
x = np.arange(0, 5, 0.1)  # 生成0-5，间隔为0.1的小数
y1 = np.sin(np.pi * x)
y2 = np.sin(np.pi * x + np.pi / 2)
plt.plot(x, y1, "g", x, y2, "b--")  # 在添加图例时，一定要先有plot()进行画画！！
plt.legend(["sin(x)", "cos(x)", "dd"], loc='upper right')
plt.show()

# 坐标系型图
# plt.axis() # 定义x轴y轴的取值范围
x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y1 = np.sin(3 * x) / x
y2 = np.sin(2 * x) / x
y3 = np.sin(x) / x
plt.plot(x, y1, "-", x, y2, "--", x, y3, "-.", linewidth=2.5)
# 改变x轴y轴坐标，可改成希腊字母，要用到LaTeX表达式的字符串。
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi], [r"$-2\pi$", r"$-\pi$", r"$0$", r"$+\pi$", r"$+2\pi$"])
plt.yticks([-1, 0, 1, 2, 3], [r'$-1$', r'$0$', r'$+1$', r'$+2$', r'$+3$'])
# 设置笛卡尔坐标系
ax = plt.gca()
ax.spines['right'].set_color('none')  # 将axes的右侧边框设置为无色
ax.spines['top'].set_color('none')  # 将axes的上侧边框设置为无色
ax.xaxis.set_ticks_position('bottom')  # 移动下边框到中间
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')  # 移动左边框到中间
ax.spines['left'].set_position(('data', 0))
plt.show()

# 为pandas绘制线型图
# 用matplotlib库把pandas库的DataFrame数据结构绘制成图表
frame = pd.DataFrame({'adam': [1, 3, 4, 3, 5],
                      'bob': [2, 4, 5, 2, 4],
                      'simon': [3, 2, 3, 1, 3]},
                     index=['A', 'B', 'C', 'D', 'E'])
# Series在Dataframe中是以竖列的形式排列的
print(frame)
plt.axis([0, 4, 0, 7])
x = np.arange(5)
plt.plot(x, frame, '-', linewidth=2)
plt.legend(frame, loc='upper left')
plt.show()

# 绘制直方图 ——>hist()函数
# 直方图的更多代码方法详见 https://www.runoob.com/matplotlib/matplotlib-hist.html
pop = np.random.randint(0, 100, 100)  # 生成一组随机数据
# 绘制直方图
n1, n2, n3 = plt.hist(pop, bins=20)  # hist()不仅能绘制直方图，还能以元组的方式返回计算值（每个面元包含的样本个体数量）
# 设置图表属性
plt.title('Adam')
plt.xlabel("value")
plt.ylabel("frequency")
plt.show()

# 绘制条状图 ——>bar()函数
# 绘制水平条状图 ——>barh()函数

# 绘制多序列条状图
index = np.arange(5)
values1 = [5, 7, 3, 4, 6]
values2 = [3, 5, 6, 5, 7]
values3 = [5, 6, 7, 4, 6]
plt.axis([0, 5, 0, 8])
bw = 0.3
plt.title('A Multiseries Bar Chart', fontsize=20)
plt.bar(index + 0.5 * bw, values1, width=bw, color='b')  # 对于数值一定要计算准确
plt.bar(index + 1.5 * bw, values2, width=bw, color='g')
plt.bar(index + 2.5 * bw, values3, width=bw, color='r')
plt.xticks(index + 0.45, ['A', 'B', 'C', 'D', 'E'])
plt.show()

# 为pandas绘制多序列条状图
# pandas 绘制多序列条状图可快速完成，实现自动化。
# 如果想对图标的绘制过程拥有更多的控制权，可以从DataFrame中抽取数据，保存为NumPy数组，把他们作为一个个单独的数据分别传给matplotlib函数。（类似于上面的那部分）
index = np.arange(5)
frame = pd.DataFrame({'values1': [5, 7, 3, 4, 6],
                      'values2': [3, 5, 6, 5, 7],
                      'values3': [5, 6, 7, 4, 6]}, index=['A', 'B', 'C', 'D', 'E'])
print(frame)
frame.plot(kind="bar")
plt.show()

# 多序列堆积条状图(堆叠状，一层一层)
series1 = np.array([3, 4, 5, 3])
series2 = np.array([1, 2, 2, 5])
series3 = np.array([2, 3, 3, 4])
x = np.arange(0, 4, 1)
plt.axis([0, 4, 0, 15])
do = 0.5
plt.bar(x + do, series1, width=0.75, color='red')
plt.bar(x + do, series2, width=0.75, color='blue', bottom=series1)
plt.bar(x + do, series3, width=0.75, color='orange', bottom=(series2 + series1))
plt.xticks(x + do, ['A', 'B', 'C', 'D'])
plt.show()

# 为pandas绘制堆积条状图
# # pandas 绘制堆积条状图可快速完成，实现自动化。与多序列条状图不同的是，只需要在plot()函数中打开stacked开关
frame = pd.DataFrame({'values1': [5, 7, 3, 4, 6],
                      'values2': [3, 5, 6, 5, 7],
                      'values3': [5, 6, 7, 4, 6]}, index=['A', 'B', 'C', 'D', 'E'])
frame.plot(kind='bar', stacked=True)
plt.show()

# 其他条状图(表示对比关系非常实用)
xo = np.arange(8)
y1 = np.array([1, 3, 4, 6, 4, 3, 2, 1])
y2 = np.array([1, 2, 5, 4, 3, 3, 2, 1])
plt.axis([0, 8, -7, 7])
plt.bar(xo + 0.45, y1, 0.9, facecolor='r', edgecolor='w')
plt.bar(xo + 0.45, -y2, 0.9, facecolor='b', edgecolor='w')
plt.grid(False)
for x, y in zip(xo, y1):
    plt.text(x + 0.45, y + 0.05, '%d' % y, ha='center', va='bottom')
for x, y in zip(xo, y2):
    plt.text(x + 0.45, -y - 0.05, '%d' % y, ha='center', va='top')
plt.show()

# 其他图
# 饼图
# 高级图表
# 参考网站 https://www.runoob.com/w3cnote/matplotlib-tutorial.html
#        https://www.runoob.com/matplotlib/matplotlib-scatter.html
