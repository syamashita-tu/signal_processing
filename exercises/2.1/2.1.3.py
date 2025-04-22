# 必要なライブラリの再インポート（コード実行状態がリセットされたため）
import numpy as np
import matplotlib.pyplot as plt

# ランプ関数 r[n] の定義
def r(n):
    return np.where(n >= 0, n, 0)

# N の設定
N = 5
n = np.arange(-2, 10)

# x[n] = r[n] - r[n - N]
x = r(n) - r(n - N)

# プロット
plt.stem(n, x)
plt.title(r'$x[n] = r[n] - r[n - N]$, $N=5$')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.tight_layout()

plt.savefig("./exercises/2.1/fig/2.1.3.png")
