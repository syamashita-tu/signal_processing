import numpy as np
import matplotlib.pyplot as plt

# ステップ関数 u_0[n] の定義
def u0(n):
    return np.where(n >= 0, 1, 0)

# n の範囲
n = np.arange(-5, 10)

# α の候補
alphas = [-2, -1, -0.5, 0.5, 1, 2]

# n を float 型で扱うよう修正
n = np.arange(-5, 10)

# プロット準備
fig, axs = plt.subplots(2, 3, figsize=(15, 6))
axs = axs.flatten()

# 各 α に対する x[n] = α^n * u_0[n] を描画（指数演算に float を使用）
for i, alpha in enumerate(alphas):
    x = (alpha ** n.astype(float)) * u0(n)
    axs[i].stem(n, x)
    axs[i].set_title(fr'$\alpha = {alpha}$')
    axs[i].set_xlabel('n')
    axs[i].set_ylabel('x[n]')
    axs[i].grid(True)

plt.tight_layout()

# 保存
plt.savefig("./exercises/2.1/fig/2.1.5.png")
