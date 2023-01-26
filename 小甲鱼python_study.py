# 小甲鱼python
变量与字符串 = 0  # 中文可作为变量名
print("变量与字符串: ", 变量与字符串)
变量与字符串 = "变量与字符串"
print("变量与字符串: ", 变量与字符串)
x = 3
y = 4
print(x, y)
x, y = y, x
print(x, y)

print("let's go!")
print('"life is short, you need Python. "')
print('\"life is short, \nlet\'s go! \"')
print("D:\anaconda3\python.exe\n")
print(r"D:\anaconda3\python.exe\n")
print("beard\n\
now")  # "\n\"末尾”\“为换行写
text = '''在这里我们介绍了什么是机器学习, 还有机器学习包含了哪些方法. 通常来说, 机器学习的方法包括:

监督学习 supervised learning;
非监督学习 unsupervised learning;
半监督学习 semi-supervised learning;
强化学习 reinforcement learning;
遗传算法 genetic algorithm.
大家就在影片中看看这些方法究竟都有哪些不同吧.'''
print(text)

print("每天爱你！\n" * 5)

import random

x = random.getstate()  # 随机数状态
print(x)
random.setstate(x)
tmp = random.randint(10, 20)  # 随机获取10~20的整数
print(tmp)

# 传回随机数状态，重现随机数
random.setstate(x)
tmp = random.randint(10, 20)  # 随机获取10~20的整数
print(tmp)

# 数字类型，精度问题
i = 0
while i < 1:
    print(i)
    i += 0.1
print(0.1+0.2)
print(0.3)
print(0.3 == 0.1+0.2)

# 精确计算浮点数
import decimal
print(decimal.Decimal('0.1') + decimal.Decimal('0.2'))
print(decimal.Decimal('0.3') == decimal.Decimal('0.1') + decimal.Decimal('0.2'))

# 科学计数法
print(1e-05)
# 复数
print(1+2j, (1+2j).real, (1+2j).imag)

# //向下取整，即floor
print(-3//2)    # 答案为-2
# 取余
print(-3 % 2)
# 同时求floor与mod
print(divmod(-3, 2))

# 取绝对值或模
print(abs(1+2j))

# 转换为复数
print(complex("1+2j"))
print(complex("1"))

# pow函数与**的区别
print(pow(2, 3, 5))    # 等价于2 ** 3 % 5

import decimal as dec
import fractions as frac
# bool函数
print(bool(0))
# 定义为false的值
print(bool(0), "\n",
      bool(0.0), "\n",
      bool(0j), "\n",
      bool(dec.Decimal(0)), "\n",
      bool(frac.Fraction(0,1)), "\n",  # Fraction(x, y)约分
      bool(None), bool(False), "\n",
      bool(''), bool(()), bool([]), bool({}), bool(set()), bool(range(0)))

print(frac.Fraction(6,9))   # 结果为2/3
print(frac.Fraction(dec.Decimal('5.418')))  # 将小数转为最简分式
print(frac.Fraction(6,9).denominator, frac.Fraction(6,9).numerator)
    # denominator为分母，denominator为分子

# &&:and    ||:or   !:not   and、or满足短路运算
# 优先级
print(3<4 and 4<5)
print(3<4 and 4>5)
print(3<4 or 4<5)
print(3<4 or 4>5)
print(not 4<5)
print(3 and 4)
print(3 or 4)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
mylist[1] = "mnk"
print(thislist)
print(mylist)

thisset = {"apple", "banana", "cherry"}

thisset.update(("orange", "mango", "grapes"))

print(thisset)

thisdict = {
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
thisdict["year"] = 2019
print(thisdict)
for x in thisdict:
    print(x)
for x in thisdict.values():
    print(x)
for x in thisdict:
    print(thisdict[x])
for x, y in thisdict.items():
    print(x, y)
thisdict = {
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
thisdict.popitem()
print(thisdict)
car = {
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}

x = car.pop("md",1963)

print(x)
print(car)

def my_function(fname):
  print(fname + " Gates")

my_function("Rory John")
my_function("Jennifer Katharine")
my_function("Phoebe Adele")
