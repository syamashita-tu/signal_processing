import numpy as np
import matplotlib.pyplot as plt
import os

# 定義域とパラメータ再定義
n = np.arange(0, 50)
alphas = [-2, -1, -0.5, 0.5, 1, 2]

# サブプロット設定
fig, axs = plt.subplots(2, 3, figsize=(18, 8))
axs = axs.flatten()

# 各αのスペクトルをプロット
for i, alpha in enumerate(alphas):
    x_n_alpha = alpha**n
    X_k_alpha = np.fft.fft(x_n_alpha, n=512)
    freq_alpha = np.fft.fftfreq(len(X_k_alpha), d=1)
    amplitude_spectrum_alpha = np.abs(X_k_alpha)

    axs[i].plot(freq_alpha, amplitude_spectrum_alpha)
    axs[i].set_title(f"$\\alpha$ = {alpha}")
    axs[i].set_xlim(0, 0.5)
    axs[i].set_xlabel("Frequency")
    axs[i].set_ylabel("Amplitude")
    axs[i].grid(True)


# レイアウト調整
plt.tight_layout()
combined_path = "./exercises/2.2/fig/2.2.5.png"
plt.savefig(combined_path)
plt.close()

combined_path
