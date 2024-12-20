import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
n = np.array([0, 1, 2, 3, 4])
T_ms = np.array([1586.011, 1672.654, 1755.244, 1833.753, 1909.52])
T_s = T_ms / 1000  # 将时间单位从毫秒转换为秒
m1 = (213.03+2.60) / 1000  # 滑块加条形挡光片质量，单位为kg
m2 = 25.02 / 1000    # 骑码质量，单位为kg
m = m1 + n * m2  # 总质量，单位为kg

# 进行线性拟合
coefficients = np.polyfit(m, T_s**2, 1)
poly = np.poly1d(coefficients)

# 计算相关系数
correlation_matrix = np.corrcoef(m, T_s**2)
correlation_coefficient = correlation_matrix[0, 1]

# 拟合结果
print(f"拟合得到的系数: {coefficients}")
print(f"相关系数: {correlation_coefficient}")

# 绘图
plt.scatter(m, T_s**2, label='实验数据')
plt.plot(m, poly(m), label='拟合曲线', color='red')

# 显示图线方程和相关系数
equation_text = f'$T^2 = {coefficients[0]:.4f} \cdot m + {coefficients[1]:.4f}$\n相关系数: {correlation_coefficient:.4f}'
plt.text(0.45, 0.45, equation_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

plt.xlabel('质量 $m$ (kg)')
plt.ylabel('周期平方 $T^2$ (s$^2$)')
plt.legend()
plt.title('$T^2 - m$ 拟合')
plt.show()