import numpy as np
import matplotlib.pyplot as plt

# ランプ関数の再定義
def r(n):
    return np.where(n >= 0, n, 0)

# N の設定
N = 5
n = np.arange(-2, 20)

# x[n] = r[n] - 2*r[n - N] + r[n - 2N]
x = r(n) - 2 * r(n - N) + r(n - 2 * N)

# プロット
plt.stem(n, x)
plt.title(r'$x[n] = r[n] - 2r[n - N] + r[n - 2N]$, $N=5$')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()

plt.savefig("./exercises/2.1/fig/2.1.4.png")

