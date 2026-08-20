# Day 1. 一个神经元
import math

def neuron(inputs, weights, bias):
    # 公式：inputs * weights + bias
    z = sum(x * w for x, w in zip(inputs, weights)) + bias
    # zip 会把两个列表对应位置的元素配对.
    # 把 inputs 和 weights 中对应位置的元素一对一取出来，分别赋给 x 和 w.
    return 1 / (1 + math.exp(-z))
    # 使用Sigmoid激活函数。

# 场景：今晚要不要点外卖？
# 输入：[加班时长, 冰箱余粮, 下雨成都]，归一化到 0~1
# 归一化：把原来单位、数值范围不同的数据，统一转换到 0 到 1 之间。
x = [0.9, 0.1, 0.7] # 输入
w = [0.8, -0.6, 0.3] # 权重
b = -0.2 # 偏置

p = neuron(x, w, b)
print(f"点外卖概率: {p:.2f}")