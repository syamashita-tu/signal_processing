import numpy as np
import matplotlib.pyplot as plt

# 信号定義
N = 5
x = np.ones(N)
X = np.fft.fft(x)
amplitude_spectrum = np.abs(X)

# 英語でプロット
plt.figure(figsize=(8, 4))
plt.stem(np.arange(N), amplitude_spectrum)
plt.xlabel('Frequency index $k$')
plt.ylabel('Amplitude $|X[k]|$')
plt.title(f'Amplitude Spectrum (N = {N})')
plt.grid(True)
plt.tight_layout()
plt.savefig("./exercises/2.2/fig/2.2.1.png")
