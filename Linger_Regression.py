import random

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 线性回归算法
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[(np.ones((100, 1)), X)]
# theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)  # np.linalg.inv()进行矩阵的逆运算
X_new = np.array([[0], [2]])
X_new_b = np.c_[(np.ones((2, 1)), X_new)]
# y_predict = X_new_b.dot(theta_best)
# print(theta_best)

# # 利用包进行线性回归训练模型
# lin_reg = LinearRegression()
# lin_reg.fit(X, y)
# # print(lin_reg.coef_, lin_reg.intercept_)

# # 线性回归梯度下降
# # 批量梯度下降（对所有数据进行多次遍历）
# theta_path_bgd = []
#
#
# def polt_gradient_descent(theta, eta, theta_path=None):
#     m = len(X_b)
#     plt.plot(X, y, 'b.')
#     n_iterations = 1000
#     for iterations in range(n_iterations):
#         y_predict = X_new_b.dot(theta)
#         plt.plot(X_new, y_predict, 'k')
#         gradients = 2 / m * X_b.T.dot(X_b.dot(theta) - y)
#         theta = theta - eta * gradients
#         if theta_path is not None:
#             theta_path.append(theta)
#         plt.xlabel('x_1')
#         plt.axis([0, 2, 0, 15])
#         plt.title('eta = {}'.format(eta))
#
#
# theta = np.random.randn(2, 1)
# plt.figure(figsize=(10, 4))
# plt.subplot(131)
# polt_gradient_descent(theta, eta=0.02)
# plt.subplot(132)
# polt_gradient_descent(theta, eta=0.1)
# plt.subplot(133)
# polt_gradient_descent(theta, eta=0.5)
# plt.show()

# # 随机梯度下降
# theta_path_sgd = []  # 将更新过的theta值存入一个列表
# m = len(X_b)  # 计算样本数量
# n_epochs = 50  # 指定迭代多少遍，指定epochs
#
# t0 = 5
# t1 = 50
#
#
# def learning_schedule(t):  # 指定衰减策略（学习率的衰减）
#     return t0 / (t1 + t)  # t越大学习率在逐渐衰减
#
#
# theta = np.random.randn(2, 1)
# print(theta)
# for epoch in range(n_epochs):  # 遍历整个样本n_epochs次
#     for i in range(m):  # 分别在每次中遍历样本数据
#         if epoch < 10 and i < 20:  # 由于数据太大，画图太乱，我们对遍历次数进行限制
#             y_predict = X_new_b.dot(theta)  # 预测结果值
#             plt.plot(X_new, y_predict, 'k')  # 将预测结果进行展示
#         random_index = np.random.randint(m)  # 选择随机数据进行迭代，随机索引
#         xi = X_b[random_index:random_index + 1]  # 将随机索引传入
#         yi = y[random_index:random_index + 1]  # 将随机索引传入
#         gradients = 2 * xi.T.dot(xi.dot(theta) - yi)  # 计算下降梯度的梯度值
#         eta = learning_schedule(n_epochs * m + i)  # 计算新学习率，学习率进行衰减，迭代了(n_epochs * m + i)次
#         theta = theta - eta * gradients  # 更新theta值
#         theta_path_sgd.append(theta)  # 将更新过的theta值存入一个列表
# print(theta_path_sgd[1])
# plt.plot(X, y, 'r.')
# plt.axis([0, 2, 0, 15])
# plt.show()

# # 小批量梯度下降(minibatch)
# theta_path_mgd = []  # 将每次迭代计算的theta值存入列表
# n_epochs = 50  # 指定迭代次数
# minibatch = 16  # 一般指定2的几次幂
# theta = np.random.randn(2, 1)
# t = 0
# t0 = 5
# t1 = 50
#
#
# def learning_schedule(t):  # 指定衰减策略（学习率的衰减）
#     return t0 / (t1 + t)  # t越大学习率在逐渐衰减
#
#
# for epoch in range(n_epochs):  # 进行洗牌操作，打乱顺序
#     m = len(X_b)  # 由于小批量选取样本数据，需要打乱样本的数据，因此计算样本的数量
#     shuffled_indices = np.random.permutation(m)  # 得到0——m（样本数量）的索引值，之后可以用随机的索引值得到相应的样本数据
#     X_b_shuffled = X_b[shuffled_indices]  # 利用打乱的索引值得到X样本数据
#     y_shuffled = y[shuffled_indices]  # 利用打乱的索引值得到y样本数据
#     for i in range(0, m, minibatch):  # 利用递归的思想对数据进行遍历
#         y_predict = X_new_b.dot(theta)  # 得到预测y值
#         plt.plot(X_new, y_predict, 'k')  # 画图
#         t += 1  # 对学习率函数的参数值进行迭代
#         xi = X_b_shuffled[i:i + minibatch]  # 选取每次的小批量样本数据包，每个小批量数据包的样本数据为minibatch
#         yi = y_shuffled[i:i + minibatch]  # 同上
#         gradients = 2 / minibatch * xi.T.dot(xi.dot(theta) - yi)  # 梯度下降计算坡度
#         eta = learning_schedule(t)  # 利用之前写的学习率衰减函数计算新的学习率
#         theta = theta - eta * gradients  # 计算通过梯度下降计算到的新的theta
#         theta_path_mgd.append(theta)
# plt.plot(X, y, 'r.')
# plt.axis([0, 2, 0, 15])
# plt.show()

# 多项式回归（y = ax^2+bx+c）
from sklearn.preprocessing import PolynomialFeatures

m = 100
X = 6 * np.random.rand(m, 1) - 3  # 处于-3——3的100个随机数
y = 0.5 * X ** 2 + X + np.random.rand(m, 1)
poly_features = PolynomialFeatures(degree=2, include_bias=False) # degree太高会使模型复杂度过高，导致过拟合。
X_poly = poly_features.fit_transform(X)
# print(X_poly[0])
# print(X[0]**2)
lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)  # 得到训练后的回归方程的参数
# print(lin_reg.coef_)  # 第一个值为一次项系数，第二个值为二次项系数（权重参数）
# print(lin_reg.intercept_)  # 是常数项的值
X_new = np.linspace(-3, 3, 100).reshape(100, 1)
X_new_poly = poly_features.fit_transform(X_new)
# print(X_new[0])
# print(X_new_poly[0])
y_predict = lin_reg.predict(X_new_poly)
# 画图
plt.figure()
plt.axis([-3, 3, 0, 5])
plt.plot(X, y, 'b.', label='Raw data')
plt.plot(X_new, y_predict, 'r--', label='Prediction')
plt.legend(loc='upper left')
plt.xlabel('x_')
plt.ylabel('y_')
plt.title('Polynomial Regression')
plt.show()
# 这里有个包可以进行流水线生产作业Pipeline 数据poly——>标准化——>预测
