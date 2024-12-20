import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
V = np.array([143.01, 136.28, 129.55, 115.41, 97.99]) / 100  # 将速度除以100
x = np.array([10, 15, 20, 25, 30]) / 100  # 将位移除以100

# 转化为平方
V_squared = V**2
x_squared = x**2

# 进行线性拟合
coefficients = np.polyfit(x_squared, V_squared, 1)
poly = np.poly1d(coefficients)

# 计算相关系数
correlation_matrix = np.corrcoef(x_squared, V_squared)
correlation_coefficient = correlation_matrix[0, 1]

# 拟合结果
print(f"拟合得到的系数: {coefficients}")
print(f"相关系数: {correlation_coefficient}")

# 绘图
plt.scatter(x_squared, V_squared, label='实验数据')
plt.plot(x_squared, poly(x_squared), label='拟合曲线', color='red')

# 显示图线方程和相关系数
equation_text = f'$V^2 = {coefficients[0]:.4f} \cdot x^2 + {coefficients[1]:.4f}$\n相关系数: {correlation_coefficient:.4f}'
plt.text(0.35, 0.85, equation_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

plt.xlabel('位移平方 $x^2$ (m$^2$)')
plt.ylabel('速度平方 $V^2$ (m$^2$/s$^2$)')
plt.legend()
plt.title('$V^2 - x^2$ 拟合')
plt.show()