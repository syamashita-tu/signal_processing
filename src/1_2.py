import numpy as np    # 数値計算ライブラリを別名 np として読み込み
import matplotlib.pyplot as plt    # グラフ描画ライブラリを別名 plt として読み込み
import matplotlib
matplotlib.use('TkAgg')

beta = 0.39    # パラメータの設定
alpha = 0.61    # パラメータの設定
nend = 5    # 終了時刻
n = np.arange(0, nend + 1)    # 時刻の範囲
x = np.ones(nend + 1)    # 単位ステップ入力
y = np.zeros(nend + 1)    # 出力信号の初期化
y[0] = beta * x[0]    # 出力 y[0] の計算

for m in range(1, nend + 1):    # 時刻 m = 1, ..., nend まで繰り返し
    y[m] = alpha * y[m - 1] + beta * x[m]    # 出力 y[m] の計算（差分方程式）

print('y = \n', y)    # 出力信号値の表示

fig = plt.figure()    # Figure の生成
ax = fig.add_subplot(1, 1, 1)    # 1 行 1 列に分割し、1 番目に図示
ax.stem(n, y)    # 出力の図示
ax.set_xlim(0, nend); ax.set_ylim(0, 1.5)    # 座標軸の範囲の指定
ax.grid()    # 格子の図示
ax.set_xlabel('Time $n$')    # 座標軸名の設定（x 軸）
ax.set_ylabel('Output $y[n]$')    # 座標軸名の設定（y 軸）
#plt.savefig("./data/1_2.png")

