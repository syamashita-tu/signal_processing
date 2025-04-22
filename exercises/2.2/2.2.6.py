# 再定義を行って，paramsを含めた完全なプロットを実行

import numpy as np
import matplotlib.pyplot as plt
import os

# パラメータと定義域
n = np.arange(0, 50)
params = [(0.8, np.pi / 8), (1.2, np.pi / 8)]
titles = [
    "$x[n] = r^n e^{j\\theta n}, r=0.8$",
    "$x_r[n] = r^n \\cos(\\theta n), r=0.8$",
    "$x_i[n] = r^n \\sin(\\theta n), r=0.8$",
    "$x[n] = r^n e^{j\\theta n}, r=1.2$",
    "$x_r[n] = r^n \\cos(\\theta n), r=1.2$",
    "$x_i[n] = r^n \\sin(\\theta n), r=1.2$",
]

# プロット準備
fig, axs = plt.subplots(2, 3, figsize=(18, 8))
axs = axs.flatten()

# 各信号に対するFFTと描画
for i, (r_val, theta) in enumerate(params):
    x_n_complex = (r_val ** n) * np.exp(1j * theta * n)
    x_n_real = (r_val ** n) * np.cos(theta * n)
    x_n_imag = (r_val ** n) * np.sin(theta * n)

    X_k_complex = np.fft.fft(x_n_complex, n=512)
    X_k_real = np.fft.fft(x_n_real, n=512)
    X_k_imag = np.fft.fft(x_n_imag, n=512)

    freq = np.fft.fftfreq(512, d=1)

    axs[i * 3 + 0].plot(freq, np.abs(X_k_complex))
    axs[i * 3 + 0].set_title(titles[i * 3 + 0])
    axs[i * 3 + 0].set_xlim(0, 0.5)
    axs[i * 3 + 0].grid(True)

    axs[i * 3 + 1].plot(freq, np.abs(X_k_real))
    axs[i * 3 + 1].set_title(titles[i * 3 + 1])
    axs[i * 3 + 1].set_xlim(0, 0.5)
    axs[i * 3 + 1].grid(True)

    axs[i * 3 + 2].plot(freq, np.abs(X_k_imag))
    axs[i * 3 + 2].set_title(titles[i * 3 + 2])
    axs[i * 3 + 2].set_xlim(0, 0.5)
    axs[i * 3 + 2].grid(True)

# 軸ラベルと保存
for ax in axs:
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Amplitude")

plt.tight_layout()
final_path = "./exercises/2.2/fig/2.2.6.png"
os.makedirs(os.path.dirname(final_path), exist_ok=True)
plt.savefig(final_path)
plt.close()

final_path
