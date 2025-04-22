# 二項係数列に対するFFTと振幅スペクトルの保存（指定された保存パス）

import numpy as np
import matplotlib.pyplot as plt
import math
import os

# 出力先ディレクトリ作成
output_path = "./exercises/2.2/fig/2.2.7.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Nの値のリスト
Ns = [1, 2, 3, 4]

# 図の準備
fig, axs = plt.subplots(2, 2, figsize=(14, 8))
axs = axs.flatten()

# 各Nに対して処理
for i, N in enumerate(Ns):
    n = np.arange(0, N + 1)
    x_n = np.array([math.factorial(N) // (math.factorial(k) * math.factorial(N - k)) for k in n])
    x_padded = np.pad(x_n, (0, 512 - len(x_n)), 'constant')
    X_k = np.fft.fft(x_padded)
    freq = np.fft.fftfreq(len(X_k), d=1)
    amplitude = np.abs(X_k)

    axs[i].plot(freq, amplitude)
    axs[i].set_xlim(0, 0.5)
    axs[i].set_title(f"$x[n] = \\binom{{{N}}}{{n}}$")
    axs[i].set_xlabel("Frequency")
    axs[i].set_ylabel("Amplitude")
    axs[i].grid(True)

plt.tight_layout()
plt.savefig(output_path)
plt.close()

output_path
