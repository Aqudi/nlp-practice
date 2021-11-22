import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.figure(1)
plt.grid()
plt.plot(x, y, 'g')
plt.plot([0, 0], [1.0, 0.0], ':')
plt.title('Sigmoid Function')

# 가중치 변화에 따른 Sigmoid 함수의 변화 확인
y1_w = sigmoid(0.5 * x)
y2_w = sigmoid(2 * x)

fig = plt.figure(2)
plt.suptitle('Sigmoid Function')
ax1 = fig.add_subplot(2, 1, 1)
ax1.plot(x, y, linestyle='-', label="W=1, b=0")
ax1.plot(x, y1_w, linestyle='--', label="W=0.5")
ax1.plot(x, y2_w, linestyle='--', label="W=2")
ax1.plot([0, 0], [1.0, 0.0], ':')
ax1.grid()
ax1.legend()

# 가중치 변화에 따른 Sigmoid 함수의 변화 확인
y1_b = sigmoid(x - 1)
y2_b = sigmoid(x + 1)

ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(x, y, linestyle='-', label="W=1, b=0")
ax2.plot(x, y1_b, linestyle=':', label="b=-1")
ax2.plot(x, y2_b, linestyle=':', label="b=1")
ax2.plot([0, 0], [1.0, 0.0], ':')
ax2.grid()
ax2.legend()
plt.savefig("./7-5.sigmoid.png")
