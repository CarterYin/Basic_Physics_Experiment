import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据
A = np.array([10, 15, 20, 25, 30]) / 100  # 将振幅除以100
V_max = np.array([39.85, 56.03, 74.96, 94.38, 114.99]) / 100  # 将最大速度除以100

# 转化为平方
A_squared = A**2
V_max_squared = V_max**2

# 进行线性拟合
coefficients = np.polyfit(A_squared, V_max_squared, 1)
poly = np.poly1d(coefficients)

# 计算相关系数
correlation_matrix = np.corrcoef(A_squared, V_max_squared)
correlation_coefficient = correlation_matrix[0, 1]

# 拟合结果
print(f"拟合得到的系数: {coefficients}")
print(f"相关系数: {correlation_coefficient}")

# 绘图
plt.scatter(A_squared, V_max_squared, label='实验数据')
plt.plot(A_squared, poly(A_squared), label='拟合曲线', color='red')

# 显示图线方程和相关系数
equation_text = f'$V_{{max}}^2 = {coefficients[0]:.4f} \cdot A^2 + {coefficients[1]:.4f}$\n相关系数: {correlation_coefficient:.4f}'
plt.text(0.25, 0.85, equation_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

plt.xlabel('振幅平方 $A^2$ (m$^2$)')
plt.ylabel('最大速度平方 $V_{max}^2$ (m$^2$/s$^2$)')
plt.legend()
plt.title('$V_{max}^2 - A^2$ 拟合')
plt.show()