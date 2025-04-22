import numpy as np
import matplotlib.pyplot as plt
import os

# 必要な変数を再定義してから，スペクトル解析を再実行

# パラメータと定義
N = 5
n = np.arange(-10, 30)  # 2Nまで扱うので範囲を拡大

# ランプ関数 r[n] の定義
r = lambda n: n * (n >= 0)

# x[n] = r[n] - 2r[n - N] + r[n - 2N]
x_n_combined = r(n) - 2 * r(n - N) + r(n - 2 * N)

# FFT
X_k_combined = np.fft.fft(x_n_combined, n=512)
freq_combined = np.fft.fftfreq(len(X_k_combined), d=1)
amplitude_spectrum_combined = np.abs(X_k_combined)

# プロット
plt.figure(figsize=(10, 4))
plt.plot(freq_combined, amplitude_spectrum_combined)
plt.title("Amplitude Spectrum of x[n] = r[n] - 2r[n-N] + r[n-2N]")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 0.5)
plt.tight_layout()

# 保存先
output_path_combined = "./exercises/2.2/fig/2.2.4.png"
os.makedirs(os.path.dirname(output_path_combined), exist_ok=True)
plt.savefig(output_path_combined)

output_path_combined
