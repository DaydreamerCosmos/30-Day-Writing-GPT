# Day 4. 损失函数
import math
import numpy as np

# 1. 均方误差MCE.
def mse(y, t):
    return 0.5 * np.sum((y - t)**2)

#2. 交叉熵误差CEE。
def cee(y, t):
    return -np.sum(y * np.log(y + 1e-7))
