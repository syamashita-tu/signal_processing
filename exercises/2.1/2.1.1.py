import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
N = 5
n = np.arange(0, 10)  # 表示範囲を広くとる

# 離散時間信号 x[n] = sum_{k=0}^{N-1} δ[n-k]
x = np.zeros_like(n, dtype=int)
for k in range(N):
    x[n == k] = 1  # δ[n-k]の和

# プロット
plt.stem(n, x)
plt.title(r'$x[n] = \sum_{k=0}^{N-1} \delta[n-k]$, $N=5$')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()
plt.savefig("./exercises/2.1/fig/2.1.1.png")
