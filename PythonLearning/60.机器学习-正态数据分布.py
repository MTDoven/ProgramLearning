# 正态数据分布（Normal Data Distribution）
# 在上一章中，我们学习了如何创建给定大小且在两个给定值之间的完全随机数组。
# 在本章中，我们将学习如何创建一个将值集中在给定值周围的数组。
# 在概率论中，在数学家卡尔·弗里德里希·高斯（Carl Friedrich Gauss）提出了这种数据分布的公式之后，
# 这种数据分布被称为正态数据分布或高斯数据分布。

import numpy
import matplotlib.pyplot as plt
x = numpy.random.normal(5.0, 1.0, 100000)  #μ=5 σ=1
plt.hist(x, 100)
plt.show()
#典型的正态数据分布。
# 直方图解释
# 我们使用 numpy.random.normal() 方法创建的数组（具有 100000 个值）绘制具有 100 栏的直方图。
# 我们指定平均值为 5.0，标准差为 1.0。
# 这意味着这些值应集中在 5.0 左右，并且很少与平均值偏离 1.0。
# 从直方图中可以看到，大多数值都在 4.0 到 6.0 之间，最高值大约是 5.0。


