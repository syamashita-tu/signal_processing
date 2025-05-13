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

# 問題(2): X(e^{jω}) = (1 + cos(ω))^2 を展開
# cos^2(ω) = (1 + cos(2ω))/2 を用いて
# X(e^{jω}) = (1 + cos(ω))^2 = 1 + 2cos(ω) + cos^2(ω)
# = 1 + 2cos(ω) + (1 + cos(2ω))/2
# = 1.5 + 2cos(ω) + 0.5cos(2ω)

# よって逆DTFTは，
# x[n] = 1.5δ[n] + 1δ[n−1] + 1δ[n+1] + 0.25δ[n−2] + 0.25δ[n+2]

n2 = np.arange(-5, 6)
x2 = np.zeros_like(n2, dtype=np.float64)
x2[n2 == 0] = 1.5
x2[n2 == 1] = 1.0
x2[n2 == -1] = 1.0
x2[n2 == 2] = 0.25
x2[n2 == -2] = 0.25

plot_idtft(n2, x2, r"$X(e^{j \omega }) = {1 + \cos{ \omega }}^2$", "./data/2_4_2.png")
