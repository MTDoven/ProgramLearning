# 均值、中值和众数
# 从一组数字中我们可以学到什么？
# 在机器学习（和数学）中，通常存在三种我们感兴趣的值：
#     均值（Mean） - 平均值
#     中值（Median） - 中点值，又称中位数
#     众数（Mode） - 最常见的值
# 例如：我们已经登记了 13 辆车的速度：
# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# 什么是平均，中间或最常见的速度值？
# 要计算平均值，请找到所有值的总和，然后将总和除以值的数量：
# (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
# NumPy 模块拥有用于此目的的方法：
# 请使用 NumPy mean() 方法确定平均速度：
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed) #求平均值
print(x)

# 中值是对所有值进行排序后的中间值：
# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
# 在找到中位数之前，对数字进行排序很重要。
# NumPy 模块拥有用于此目的的方法：
# 请使用 NumPy median() 方法找到中间值：
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x,type(x)) #求中位数
#如果中间有两个数字，则将这些数字之和除以 2。
# 77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
# (86 + 87) / 2 = 86.5
import numpy
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x,type(x))    #求中位数

# 众值是出现次数最多的值：
# 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86
# SciPy 模块拥有用于此目的的方法：
# 请使用 SciPy mode() 方法查找出现次数最多的数字：
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed,keepdims=True)
print(x,type(x))
print(x[0],type(x[0]))
print(x[0][0],type(x[0][0]))
# 求众数
