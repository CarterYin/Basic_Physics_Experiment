import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据点
s_data = np.array([1, 3, 5, 10])/100
v_data = np.array([0.3264, 0.3248, 0.3249, 0.3434])

# 进行线性拟合
coefficients = np.polyfit(s_data, v_data, 1)
a, b = coefficients

# 生成拟合直线的y值
v_fit = np.polyval(coefficients, s_data)

# 计算相关系数
correlation_matrix = np.corrcoef(s_data, v_data)
correlation_coefficient = correlation_matrix[0, 1]

# 绘制数据点和拟合曲线
plt.scatter(s_data, v_data, label='数据点')
plt.plot(s_data, v_fit, color='red', label='拟合曲线')

# 添加拟合直线方程和相关系数
equation_text = f'y = {a:.4f}x + {b:.4f}\n相关系数: {correlation_coefficient:.4f}'
plt.text(0.05, 0.34, equation_text, fontsize=12, color='red')

# 添加图表标题
plt.title('v-s图')

plt.xlabel('S/m')
plt.ylabel('v/(m/s)')
plt.legend()
plt.show()