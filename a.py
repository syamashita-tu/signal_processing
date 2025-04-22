import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = './font/NotoSansJP-VariableFont_wght.ttf'  # 適宜変更
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
