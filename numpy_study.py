import numpy as np

a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
a = np.array([1, 2, 3], dtype=complex)
print(a)
dt = np.dtype('i4')
print(dt)
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a[0])
print(a[2].dtype)
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
print(a['name'])
print(a['age'])
print(a['marks'])
a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim, '\n', b)
print("------------------")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
a[0][1] = 10
print(b)
print(b.flags)
x = np.empty((3, 2), dtype=int)
print(x)
print(np.linspace(10, 20, num=50, endpoint=True, retstep=True, dtype=None))
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1, 1])
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3], [1, 1]])
cols = np.array([[0, 2], [0, 2], [0, 1]])
y = x[rows, cols]
y = x[[0, 0, 3, 3], [0, 2, 0, 2]]
print('这个数组的四个角元素是：')
print(y)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
c = a[[1, 2], [1, 2]]
d = a[..., 1:]
print(b)
print(c)
print(d)
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])
a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(a[~np.iscomplex(a)])
print(a[np.iscomplex(a)])
a = np.array([[1, 1, 0],
              [2, 1, 0],
              [3, 2, 0],
              [4, 2, 0],
              [5, 3, 0]])
b = a[(a[..., 0] > 2) & (a[..., 1] < 3), ...]  # 此行的最后的逗号和省略号可以省略
print(b)
a = np.array([[1, 2], [3, 4]], dtype='i1')
print(a, '\n')
b = np.tile(a, (2, 3))  # 2 * 3 个 A 组成新数组
print(b)
a = np.arange(6).reshape(2, 3)
print(a)
for x in np.nditer(a.T):
    print(x, end=", ")
print('\n')

for x in np.nditer(a.T.copy(order='C')):
    print(x, end=", ")
print('\n')
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x *= 2
print('修改后的数组是：')
print(a)
print("####################################")
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('修改后的数组是：')
for x in np.nditer(a, flags=['f_index'], order='C'):
    print(x, end=", ")
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)
print('\n')
print('原数组：')
print(a)
print('获取数组中一个值：')
print(np.where(a == 6))
print(a[1, 1, 0])  # 为 6
print('\n')

# 将轴 2 滚动到轴 0（宽度到深度）

print('调用 rollaxis 函数：')
b = np.rollaxis(a, 2, 0)
print(b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b == 6))
print('\n')

# 将轴 2 滚动到轴 1：（宽度到高度）

print('调用 rollaxis 函数：')
c = np.rollaxis(a, 2, 1)
print(c)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c == 6))
print('\n')

print("###########################################")
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

# 对 y 广播 x
b = np.broadcast(x, y)
# 它拥有 iterator 属性，基于自身组件的迭代器元组
print(x)
print('对 y 广播 x：')
r, c = b.iters

# Python3.x 为 next(context) ，Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))

print('\n')
# shape 属性返回广播对象的形状

print('广播对象的形状：')
print(b.shape)
print('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x, y)
c = np.empty(b.shape)

print('手动使用 broadcast 将 x 与 y 相加：')
print(c.shape)
print('\n')
c.flat = [u + v for (u, v) in b]

print('调用 flat 函数：')
print(c)
print('\n')
# 获得了和 NumPy 内建的广播支持相同的结果

print('x 与 y 的和：')
print(x + y)

a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

print('第一个数组：')
print(a)
print('\n')
# 第一个数组：
# [5 2 6 2 7 5 6 8 2 9]

print('第一个数组的去重值：')
u = np.unique(a)
print(u)
print('\n')
# 第一个数组的去重值：
# [2 5 6 7 8 9]

print('去重数组的索引数组：')
u, indices = np.unique(a, return_index=True)
print(indices)
print('\n')
# 去重数组的索引数组：
# [1 0 2 4 7 9]

print('我们可以看到每个和原数组下标对应的数值：')
print(a)
print('\n')
# 我们可以看到每个和原数组下标对应的数值：
# [5 2 6 2 7 5 6 8 2 9]
#
print('去重数组的下标：')
u, indices = np.unique(a, return_inverse=True)
print(u)
print('\n')
# 去重数组的下标：
# [2 5 6 7 8 9]
#
print('下标为：')
print(indices)
print('\n')
# 下标为：
# [1 0 2 0 3 1 2 4 0 5]

print('使用下标重构原数组：')
print(u[indices])
print('\n')
# 使用下标重构原数组：
# [5 2 6 2 7 5 6 8 2 9]

print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)
# 返回去重元素的重复数量：
# [2 5 6 7 8 9]
# [3 2 2 1 1 1]

print('将 10 左移两位：')
print(np.left_shift(10, 5))
print(np.binary_repr(np.left_shift(10, 5)))
print('\n')

# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('Runoob', 21, fillchar='*'))

print(np.char.capitalize('rUNoob'))

print(np.char.title('i like rUNoob'))

a = np.arange(6).reshape(3, 2)
wt = np.array([3, 5])
Average, q_sum = np.average(a, axis=1, weights=wt, returned=True)
print(Average)
print(q_sum)

a = np.array([[3, 7], [9, 1]])
print('我们的数组是：')
print(a)
print('\n')
print('调用 sort() 函数：')
print(np.sort(a))
print('\n')
print('按列排序：')
print(np.sort(a, axis=0))
print('\n')
# 在 sort 函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)
print('我们的数组是：')
print(a)
print('\n')
print('按 name 排序：')
print(np.sort(a, order='name'))
print(np.sort(a, order='age'))

nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
print(list((dv, nm)))
ind = np.lexsort((dv, nm))
print('调用 lexsort() 函数：')
print(ind)
print('\n')
print('使用这个索引来获取排序后的数据：')
print([nm[i] + ", " + dv[i] for i in ind])

a = np.array([[1, 2, 8], [4, 7, 5]])
print(np.msort(a))
arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print(arr[np.argpartition(arr, -2)])
# 录入了四位同学的成绩，按照总分排序，总分相同时语文高的优先
math = (10, 20, 50, 10)
chinese = (30, 50, 40, 60)
total = (40, 70, 90, 70)
# 将优先级高的项放在后面
ind = np.lexsort((math, chinese, total))

for i in ind:
    print([total[i], chinese[i], math[i]])

a = np.arange(0, 10, 0.5).reshape(4, -1)
np.savetxt("out.txt", a, fmt="%d", delimiter=",")  # 改为保存为整数，以逗号分隔
b = np.loadtxt("out.txt", delimiter=",")  # load 时也要指定为逗号分隔
print(b)
