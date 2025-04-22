import numpy as np
import matplotlib.pyplot as plt
import math


# 階乗関数（NumPy配列に対応）
def factorial(n):
    return np.array([math.factorial(k) for k in n])

# 二項係数関数（組合せ数）
def binomial(N, n):
    result = np.zeros_like(n, dtype=float)
    valid = (0 <= n) & (n <= N)
    k = n[valid]
    result[valid] = math.factorial(N) / (factorial(k) * factorial(N - k))
    return result

# 対象とする N のリスト
Ns = [1, 2, 3, 4]

# プロット
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
axs = axs.flatten()

for i, N in enumerate(Ns):
    n = np.arange(0, N + 3)
    x = binomial(N, n)
    axs[i].stem(n, x)
    axs[i].set_title(fr'$x[n] = \binom{{{N}}}{{n}}$')
    axs[i].set_xlabel('n')
    axs[i].set_ylabel('x[n]')
    axs[i].grid(True)

plt.tight_layout()
plt.savefig("./exercises/2.1/fig/2.1.7.png")
