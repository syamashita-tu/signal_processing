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

# 問題(4): X(e^{jω}) = e^{j(π−ω)/2} * sin(ω/2)
# e^{j(π−ω)/2} = e^{jπ/2} * e^{-jω/2} = j * e^{-jω/2}
# よって X(e^{jω}) = j * e^{-jω/2} * sin(ω/2)

# sin(ω/2) = (1/(2j))(e^{jω/2} - e^{-jω/2})
# よって X(e^{jω}) = j * e^{-jω/2} * (1/(2j))(e^{jω/2} - e^{-jω/2})
# = (1/2)(1 - e^{-jω}) = (1/2) - (1/2)e^{-jω}

# ⇒ x[n] = 0.5δ[n] − 0.5δ[n−1]

n4 = np.arange(0, 6)
x4 = np.zeros_like(n4, dtype=np.float64)
x4[n4 == 0] = 0.5
x4[n4 == 1] = -0.5


plot_idtft(n4, x4, r"$X(e^{j \omega }) = e^{j (\pi - \omega) / 2} \sin{\frac{\omega }{2}}$", "./data/2_4_4.png")
