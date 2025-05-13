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

# 問題(1): X(e^{jω}) = 1 + cos(ω)
# x[n] = δ[n] + 0.5δ[n−1] + 0.5δ[n+1]
n1 = np.arange(-5, 6)
x1 = np.zeros_like(n1, dtype=np.float64)
x1[n1 == 0] = 1
x1[n1 == 1] = 0.5
x1[n1 == -1] = 0.5

plot_idtft(n1, x1, r"$X(e^{j \omega }) = 1 + \cos{ \omega }$", "./data/2_4_1.png")
