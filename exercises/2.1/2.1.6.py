import numpy as np
import matplotlib.pyplot as plt

# 単位ステップ関数
def u0(n):
    return np.where(n >= 0, 1, 0)

# n の範囲
n = np.arange(0, 30)

# (r, θ) の設定
params = [(0.8, np.pi / 8), (1.2, np.pi / 8)]

# プロット準備
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

for i, (r, theta) in enumerate(params):
    # 複素信号とその実部・虚部
    x = (r ** n) * np.exp(1j * theta * n) * u0(n)
    xr = np.real(x)
    xi = np.imag(x)
    
    axs[i, 0].stem(n, xr)
    axs[i, 0].set_title(fr'$x_r[n] = r^n \cos(\theta n),\ r={r},\ \theta=\pi/8$')
    axs[i, 0].set_xlabel('n')
    axs[i, 0].set_ylabel('x_r[n]')
    axs[i, 0].grid(True)

    axs[i, 1].stem(n, xi)
    axs[i, 1].set_title(fr'$x_i[n] = r^n \sin(\theta n),\ r={r},\ \theta=\pi/8$')
    axs[i, 1].set_xlabel('n')
    axs[i, 1].set_ylabel('x_i[n]')
    axs[i, 1].grid(True)

plt.tight_layout()

plt.savefig("./exercises/2.1/fig/2.1.6.png")