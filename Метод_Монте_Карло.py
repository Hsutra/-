import math
import random
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from scipy import integrate

n = 7# № варианта
N = 1000 #количество точек

def triangle():
    y = []
    for i in range(0, n):
        y.append(10 * i / n)
    for i in range(n, 21):
        y.append(10 * (i - 20) / (n - 20))
    return y

def specialxt(x):
    if(x <= n):
        return (10 * x / n)
    else:
        return (10 * (x - 20) / (n - 20))

def points(a, b):
    xt = []
    yt = []
    for i in range(N):
        xt.append(random.uniform(0, a))
        yt.append(random.uniform(0, b))
    return xt, yt

def kolinto(xt, yt):
    k = 0
    for i in range(len(yt)):
        if(yt[i] < specialxt(xt[i])):
            k += 1
    return k

def drawtriangle():
    a = 20
    b = 10
    x = []
    xt, yt = points(a, b)
    z = [0] * 21
    for i in range(21):
        x.append(i)
    y = triangle()
    s = (len(z) - 1) * y[n] / 2
    S = kolinto(xt, yt) / N * a * b
    print("Площадь треугольника : ", s)
    print("Приближенная площадь треугольника по методу Монте-Карло: ", S)

    rect = patches.Rectangle((0, 0), a, b, facecolor='none', linewidth=2, edgecolor="black")
    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, color='black')
    ax.plot(x, z, color='black')
    for i in range(len(xt)):
        if(yt[i] < specialxt(xt[i])):
            ax.plot(xt[i], yt[i], 'p', color='blue')
        else:
            ax.plot(xt[i], yt[i], 'p', color='black')
    ax.add_patch(rect)
    fig.set_figheight(5)
    fig.set_figwidth(8)
    plt.show()

#-----------------------------------------------------------------------

#определение x
def shag():
    a = 0
    h = 5 / N
    x = []
    while(a < 5):
        x.append(a)
        a += h
    return x

def integral(x):
    y = []
    for i in x:
        y.append(math.sqrt(11 - n * pow(math.sin(i), 2)))
    return y

def specialxt2(x):
    return math.sqrt(11 - n * pow(math.sin(x), 2))

def kolinto2(xt, yt):
    k = 0
    for i in range(len(yt)):
        if(yt[i] < specialxt2(xt[i])):
            k += 1
    return k

def drawintegral():
    # вычисление интеграла
    f = lambda x: math.sqrt(11 - n * pow(math.sin(x), 2))
    res = integrate.quad(f, 0, 5)
    print("Значение интеграла: ", res[0])
    x = shag()
    y = integral(x)
    a = 5
    b = max(y)
    xt, yt = points(a, b)
    rect = patches.Rectangle((0, 0), a, b, facecolor='none', linewidth=2, edgecolor="black")
    S = kolinto2(xt, yt) / N * a * b
    print("Приближенное значение интеграла по методу Монте-Карло: ", S)
    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, color='black')
    ax.add_patch(rect)
    for i in range(len(xt)):
        if(yt[i] < specialxt2(xt[i])):
            ax.plot(xt[i], yt[i], 'p', color='blue')
        else:
            ax.plot(xt[i], yt[i], 'p', color='black')
    fig.set_figheight(5)
    fig.set_figwidth(8)
    plt.show()

#-----------------------------------------------------------------------

R = n

def circle():
    x = []
    y = []
    i = 0
    while(i <= 2 * R):
        x.append(R + R * math.cos(i))
        y.append(R + R * math.sin(i))
        i += 0.1
    return x, y

def drawcircle():
    x, y = circle()
    D = 2 * R
    M = 0
    rect = patches.Rectangle((0, 0), D, D, facecolor='none', linewidth=2, edgecolor="black")
    xt, yt = points(D, D)
    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, color='black')
    for i in range(len(xt)):
        if(pow(xt[i] - R, 2) + pow(yt[i] - R, 2) < pow(R, 2)):
            ax.plot(xt[i], yt[i], 'p', color='blue')
            M += 1
        else:
            ax.plot(xt[i], yt[i], 'p', color='black')
    ax.add_patch(rect)
    ax.axis('equal')
    pi = 4 * M / N
    print("Число пи:", math.pi)
    print("Приближенное значения числа пи по методу Монте-Карло:", pi)
    fig.set_figheight(5)
    fig.set_figwidth(8)
    plt.show()

#-----------------------------------------------------------------------

def polcor():
    x = []
    y = []
    i = 0
    while (i <= 2 * R):
        p = math.sqrt(18 * pow(math.cos(i), 2) + 4 * pow(math.sin(i), 2))
        x.append(p * math.cos(i))
        y.append(p * math.sin(i))
        i += 0.05
    return x, y

def points2(a, b, c, d):
    xt = []
    yt = []
    for i in range(N):
        xt.append(random.uniform(a, c))
        yt.append(random.uniform(b, d))
    return xt, yt

def ff(x, y):
    if (x > 0):
        return math.atan(y / x)
    elif (x < 0):
        return math.atan(y / x) + math.pi
    elif (y > 0):
        return math.pi / 2
    elif(y < 0):
        return 3 * math.pi / 2

def pf(a):
    return math.sqrt(18 * pow(math.cos(a), 2) + 4 * pow(math.sin(a), 2))

def drawpol():
    M = 0
    x, y = polcor()
    a = min(x)
    b = min(y)
    c = max(x)
    d = max(y)
    str1 = d - b
    str2 = c - a
    xt, yt = points2(a, b, c, d)
    pp = []
    for i in range(len(xt)):
        pp.append(math.sqrt(pow(xt[i], 2) + pow(yt[i], 2)))
    rect = patches.Rectangle((c, d), 2 * a, 2 * b, facecolor='none', linewidth=2, edgecolor="black")
    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, color='black')
    for i in range(len(xt)):
        if(pp[i] < pf(ff(xt[i], yt[i]))):
            ax.plot(xt[i], yt[i], 'p', color='blue')
            M += 1
        else:
            ax.plot(xt[i], yt[i], 'p', color='black')
    ax.add_patch(rect)
    ax.axis('equal')
    fig.set_figheight(5)
    fig.set_figwidth(8)
    f = lambda x: 18 * pow(math.cos(x), 2) + 4 * pow(math.sin(x), 2)
    res = integrate.quad(f, 0, math.pi * 2)
    print("Точная площадь фигуры: ", 1/2 * res[0])
    S = M / N * str1 * str2
    print("Приближенная площадь фигуры по Методу Монте-Карло:", S)
    plt.show()


drawtriangle()
drawintegral()
drawcircle()
drawpol()
