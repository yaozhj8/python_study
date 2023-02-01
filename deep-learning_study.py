import numpy as np
import matplotlib.pylab as plt


# 与门
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 与非门
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 仅权重和偏置与AND不同！
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 或门
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])  # 仅权重和偏置与AND不同！
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# 异或门
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


# 激活函数
# 阶跃函数，下面两个均是
def step_function(x):
    return (x > 0).astype(np.int_)


def step_function_1(x):
    return np.array(x > 0, dtype=np.int_)


# sigmoid函数的实现
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# ReLU函数
def relu(x):
    return np.maximum(0, x)


# 恒等函数
def identity_function(x):
    return x


def init_network():
    network = dict(
        W1=np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]),
        b1=np.array([0.1, 0.2, 0.3]),
        W2=np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
        b2=np.array([0.1, 0.2]),
        W3=np.array([[0.1, 0.3], [0.2, 0.4]]),
        b3=np.array([0.1, 0.2])
    )
    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)  # [ 0.31682708 0.69627909]

# 输出层的设计
"""
神经网络可以用在分类问题和回归问题上，不过需要根据情况改变输出层的激活函数。
一般而言，回归问题用恒等函数，分类问题用softmax函数
"""


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))
