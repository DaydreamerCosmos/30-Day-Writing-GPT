# Day 5. 梯度下降
w = 0.0
# w: 权重
lr = 0.3
# lr: 学习率

# 损失函数是 (w-3)**2, 要找: 什么样的 w 能让 L(w) 最小？

for i in range(1, 16):
    grad = 2 * (w-3)
    # Gradient: 梯度
    # 梯度: 对损失函数 (w-3)**2 求导
    w = w - lr * grad
    # 学习率
    if i in (1, 2, 3, 5, 10, 15):
        loss = (w - 3) ** 2
        print(f"Step {i}, w = {w: .4f}, loss = {loss: .6f}")