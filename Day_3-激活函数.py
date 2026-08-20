# Day 3. 激活函数
import math

# step 激活函数
def step(z):
    if z > 0:
        return 1
    else:
        return 0

# sigmoid 激活函数
def sigmoid(z):
    return 1/(1 + math.exp(-z))

# relu 激活函数
def relu(z):
    if z > 0:
        return z
    else:
        return 0

for z in [-2, -0.5, 0.5, 2]:
    # -2：很强的负信号。-0.5：较弱的负信号。-0.5：较弱的正信号。-2：很强的正信号。
    print(f"step = {step(z)}")
    print(f"relu = {relu(z)}")
    print(f"sigmoid = {sigmoid(z)}")
