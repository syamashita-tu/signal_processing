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

# 問題(3): X(e^{jω}) = e^{-jω/2} * cos(ω/2)
# cos(ω/2) = (e^{jω/2} + e^{-jω/2}) / 2 より
# X(e^{jω}) = e^{-jω/2} * (e^{jω/2} + e^{-jω/2}) / 2
# = (1 + e^{-jω}) / 2
# = 0.5 + 0.5e^{-jω}
# ⇒ x[n] = 0.5δ[n] + 0.5δ[n−1]

n3 = np.arange(0, 6)
x3 = np.zeros_like(n3, dtype=np.float64)
x3[n3 == 0] = 0.5
x3[n3 == 1] = 0.5


plot_idtft(n3, x3, r"$X(e^{j \omega }) = e^{j \omega / 2} \cos{\frac{\omega }{2}}$", "./data/2_4_3.png")
