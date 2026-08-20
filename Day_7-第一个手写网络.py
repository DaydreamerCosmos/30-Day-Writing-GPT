import math, random
random.seed(42)
sig = lambda x:1 / (1 + math.exp(-x))
data = [([0,0],0),([0,1],1),([1,0],1),([1,1],0)] # XOR
w = [random.uniform(-1,1) for _ in range(9)] # 9 个参数

for epoch in range(5001):
    loss = 0
    for (x1, x2), t in data:
        # 正向传播.
        h1 = sig(w[0] * x1 + w1[1] * x2 + w2) # 隐藏神经元 1
        h2 = sig(w[4] * x1 + w[5] * x2 + w[6])
        y = sig(w[6] * h1 + w[7] * h2 + w[8])
        loss += (y - t) ** 2

        # 反向传播.
        d = 2 * (y - t) * y * t
        d1 = d * w[6] * h1 * (1 - h1)
        d2 = d * w[7] * h2 * (1 - h2)
        g = [d1 * x1, d2 * x2, d1, d2 * x1, d2 * x2, d2, d*h1, d*h2, d]

