# 変数 `n` を再定義し，続いてスペクトル解析を再実行
import numpy as np
import matplotlib.pyplot as plt
import os

# パラメータ設定
N = 5
n = np.arange(-10, 20)  # 十分な範囲で評価

# ランプ関数r[n]
r = lambda n: n * (n >= 0)

# x[n] = r[n] - r[n - N]
x_n_ramp = r(n) - r(n - N)

# FFT
X_k_ramp = np.fft.fft(x_n_ramp, n=512)
freq_ramp = np.fft.fftfreq(len(X_k_ramp), d=1)
amplitude_spectrum_ramp = np.abs(X_k_ramp)

# プロット
plt.figure(figsize=(10, 4))
plt.plot(freq_ramp, amplitude_spectrum_ramp)
plt.title("Amplitude Spectrum of x[n] = r[n] - r[n-N]")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 0.5)
plt.tight_layout()

# 保存先
output_path_ramp = "./exercises/2.2/fig/2.2.3.png"
os.makedirs(os.path.dirname(output_path_ramp), exist_ok=True)
plt.savefig(output_path_ramp)

output_path_ramp
