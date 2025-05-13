import numpy as np
import matplotlib.pyplot as plt

def plot_idtft(n, x_n, title, filename):
    plt.figure()
    plt.stem(n, x_n)  # use_line_collection を削除
    plt.xlabel(r"$n$")
    plt.ylabel(r"$x[n]$")
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)

# 問題(5): X(e^{jω}) = 1 / (1 - αe^{-jω})，|α| < 1
# これは因果的な指数関数系列：x[n] = α^n u[n]

alpha = 0.5  # 例として α = 0.5 を使用
n5 = np.arange(0, 21)
x5 = alpha**n5  # x[n] = α^n for n ≥ 0


plot_idtft(n5, x5, r"$X(e^{j \omega }) = \frac{1} {1-\alpha e^{-j\omega}} , |\alpha|<1, \alpha=0.5 $", "./data/2_4_5.png")
