import numpy as np
import matplotlib.pyplot as plt

# ステップ関数 u_0[n] の定義
def u0(n):
    return np.where(n >= 0, 1, 0)

# N の設定
N = 5
n = np.arange(-2, 10)

# x[n] = u_0[n] - u_0[n - N]
x = u0(n) - u0(n - N)

# プロット
plt.stem(n, x)
plt.title(r'$x[n] = u_0[n] - u_0[n - N]$, $N=5$')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()
plt.savefig("./exercises/2.1/fig/2.1.2.png")
