# Day 2. 权重和偏置
import math
def sigmoid(z):
    return 1 / (1 + math.exp(-z))
# 激活函数

def neuron(w, b):
    x = [0.9, 0.4, 0.5]
    # 3 个输入：很饿 0.9 / 有点懒 0.4 / 钱包还行 0.5
    z = sum(xi * wi for xi, wi in zip(x, w)) + b
    # z 是输入经过加权求和、再加上偏置后的结果。
    return sigmoid(z)
    # 把 z 映射到 0 ∼ 1; 引入非线性，让神经网络能学习复杂关系。

print("原版我：", round(neuron([0.5, 0.3, 0.4], -0.1), 2))
print("吃货我：", round(neuron([2.0, 0.3, 0.4], -0.1), 2))
print("原版我：", round(neuron([0.5, 0.3, 0.4], -2.0), 2))