import numpy as np
import matplotlib.pyplot as plt
import os

# パラメータ設定
N = 5
n = np.arange(-10, 20)  # 十分な範囲で評価

# ステップ関数u0[n]
u0 = lambda n: np.where(n >= 0, 1, 0)

# x[n] = u0[n] - u0[n - N]
x_n = u0(n) - u0(n - N)

# FFT
X_k = np.fft.fft(x_n, n=512)  # ゼロパディングで高解像度
freq = np.fft.fftfreq(len(X_k), d=1)

# 振幅スペクトル
amplitude_spectrum = np.abs(X_k)

# プロット
plt.figure(figsize=(10, 4))
plt.plot(freq, amplitude_spectrum)
plt.title("Amplitude Spectrum of x[n]")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 0.5)  # 0〜0.5の正の周波数部分を表示
plt.tight_layout()

# 保存先
output_path = "./exercises/2.2/fig/2.2.2.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)

output_path
