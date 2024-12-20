import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据点
t_data = np.array([27.79, 82.46, 135.81, 266.22])/1000
v_data = np.array([0.3598, 0.3638, 0.3682, 0.3756])

# 进行线性拟合
coefficients = np.polyfit(t_data, v_data, 1)
a, b = coefficients

# 生成拟合直线的y值
v_fit = np.polyval(coefficients, t_data)

# 计算相关系数
correlation_matrix = np.corrcoef(t_data, v_data)
correlation_coefficient = correlation_matrix[0, 1]

# 绘制数据点和拟合曲线
plt.scatter(t_data, v_data, label='数据点')
plt.plot(t_data, v_fit, color='red', label='拟合曲线')

# 添加拟合直线方程和相关系数
equation_text = f'y = {a:.4f}x + {b:.4f}\n相关系数: {correlation_coefficient:.4f}'
plt.text(0.10, 0.372, equation_text, fontsize=12, color='red')

# 添加图表标题
plt.title('v-t图')

plt.xlabel('t/s')
plt.ylabel('v/(m/s)')
plt.legend()
plt.show()