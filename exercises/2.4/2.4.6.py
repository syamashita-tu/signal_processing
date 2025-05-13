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

# 問題(6): X(e^{jω}) = 1 / (1 - 2r cos(θ)e^{-jω} + r^2 e^{-j2ω})，|r| < 1
# この形式は，2次の因果系IIRフィルタの周波数応答
# x[n] = r^n sin(θn) * u[n]

r = 0.8
theta = np.pi / 8  # 与えられた例：θ = π/8
n6 = np.arange(0, 41)
x6 = r**n6 * np.sin(theta * n6)

plot_idtft(n6, x6, r"$X(e^{j \omega }) = \frac{1} {1-2r \cos{\theta e^{-j\omega}} + r^2 e^{-j2\omega}} , |r|<1, (r,\theta)=(-0.8,\pi/8)$", "./data/2_4_6.png")
