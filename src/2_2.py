import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import art3d

# パラメータ定義
nend = 63
n = np.arange(0, nend + 1)  # 時刻の範囲
w = np.pi / 8               # 周波数
ejwn = np.exp(1j * w * n)   # 複素指数関数の計算
coswn = np.real(ejwn)       # 余弦波（実部）
sinwn = np.imag(ejwn)       # 正弦波（虚部）

# 余弦波の図示
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.stem(n, coswn, markerfmt='o')
ax1.set_xlim(0, nend)
ax1.set_ylim(-2, 2)
ax1.grid()
ax1.set_xlabel('Time $n$')
ax1.set_ylabel('Real Part')
plt.savefig("./data/2_2_1.png")

# 正弦波の図示
fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.stem(n, sinwn, markerfmt='o')
ax2.set_xlim(0, nend)
ax2.set_ylim(-2, 2)
ax2.grid()
ax2.set_xlabel('Time $n$')
ax2.set_ylabel('Imaginary Part')
plt.savefig("./data/2_2_2.png")

# 複素平面上のベクトル図
fig3 = plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.plot(coswn, sinwn, 'o')
for m in n:
    ax3.plot(np.array([0, coswn[m]]), np.array([0, sinwn[m]]))
ax3.axis('square')
ax3.set_xlim(-2, 2)
ax3.set_ylim(-2, 2)
ax3.grid()
ax3.set_xlabel('Real Part')
ax3.set_ylabel('Imaginary Part')
plt.savefig("./data/2_2_3.png")

# 複素指数関数の3次元表示
fig4 = plt.figure()
ax4 = Axes3D(fig4)
ax4.plot(n, coswn, sinwn, 'o', label='$e^{j \omega n}$')
for m, cosw, sinw in zip(n, coswn, sinwn):
    line_exp = art3d.Line3D(*zip((m, 0, 0), (m, cosw, sinw)))
    ax4.add_line(line_exp)

# 実部と虚部の平面への投影
rmax = 3
rplane = -rmax * np.ones(len(n))
iplane = -rmax * np.ones(len(n))
ax4.plot(n, coswn, rplane, 'x', label='$\cos(\omega n)$')  # 実部の投影
ax4.plot(n, iplane, sinwn, '.', label='$\sin \omega n$')   # 虚部の投影

# グラフの設定
ax4.view_init(elev=35, azim=-50)
ax4.set_xlim(0, nend)
ax4.set_ylim(-rmax, rmax)
ax4.set_zlim(-rmax, rmax)
ax4.grid()
ax4.set_xlabel('Time n')
ax4.set_ylabel('Real Part')
ax4.set_zlabel('Imaginary Part')
ax4.legend(loc='upper right')
plt.savefig("./data/2_2_4.png")

