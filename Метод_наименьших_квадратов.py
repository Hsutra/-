import numpy
import math
from matplotlib import pyplot as plt

#x = [3, 5, 7, 9, 11, 13]
#y = [3.5, 4.4, 5.7, 6.1, 6.5, 7.3]

x = [1, 2, 3, 4, 5, 6]
y = [1.0, 1.5, 3.0, 4.5, 7.0, 8.5]

pogr = {}

def sum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

#Линейная функция
def line(x, y):
    n = len(x)
    multlist = []
    squarelist = []
    for i in range(n):
        multlist.append(x[i] * y[i])  #список содержащий произведение элементов массивов x и y
    for i in range(n):
        squarelist.append(pow(x[i], 2))  #список содержащий квадраты элементов массива x

    a = (n * sum(multlist) - sum(x) * sum(y)) / (n * sum(squarelist) - pow(sum(x), 2))
    b = (sum(y) - a * sum(x)) / n
    a = round(a, 2)
    b = round(b, 2)
    s = 0
    for i in range(n):
        s += pow((a * x[i] + b - y[i]), 2)  #значение суммарной погрешности
    s = round(s, 2)
    pogr['погрешность линейной функции.'] = s
    print("Коэффициенты линейной функции: a = ", a, " b = ", b)
    print("Погрешность линейной функции: ", s)
    res = []
    for i in range(n):
        res.append(a * x[i] + b)
    return res

#Степенная функция
def stepen(x, y):
    n = len(x)
    multlist = []
    squarelist = []
    ln_x = []
    ln_y = []
    for i in range(n):
        ln_x.append(math.log(x[i]))
        ln_y.append(math.log(y[i]))
    for i in range(n):
        multlist.append(ln_x[i] * ln_y[i])
    for i in range(n):
        squarelist.append(pow(ln_x[i], 2))

    a = (n * sum(multlist) - sum(ln_x) * sum(ln_y)) / (n * sum(squarelist) - pow(sum(ln_x), 2))
    b = (sum(ln_y) - a * sum(ln_x)) / n
    a = round(a, 2)
    b = round(b, 2)
    b = pow(math.e, b)
    b = round(b, 2)
    s = 0
    for i in range(n):
        s += pow((b * pow(x[i], a) - y[i]), 2)
    s = round(s, 2)
    pogr['погрешность степенной функции.'] = s
    print("\nКоэффициенты степенной функции: a = ", a, " b = ", b)
    print("Погрешность степенной функции: ", s)
    res = []
    for i in range(n):
        res.append(b * pow(x[i], a))
    return res

#Показательная функция
def expo(x, y):
    n = len(x)
    multlist = []
    squarelist = []
    ln_y = []
    for i in range(n):
        ln_y.append(math.log(y[i]))
    for i in range(n):
        multlist.append(x[i] * ln_y[i])
    for i in range(n):
        squarelist.append(pow(x[i], 2))

    a = (n * sum(multlist) - sum(x) * sum(ln_y)) / (n * sum(squarelist) - pow(sum(x), 2))
    b = (sum(ln_y) - a * sum(x)) / n
    a = round(a, 2)
    b = round(b, 2)
    b = pow(math.e, b)
    b = round(b, 2)
    s = 0
    for i in range(n):
        s += pow((b * pow(math.e, (a * x[i])) - y[i]), 2)
    s = round(s, 2)
    pogr['погрешность показательной функции.'] = s
    print("\nКоэффициенты показательной функции: a = ", a, " b = ", b)
    print("Погрешность показательной функции: ", s)
    res = []
    for i in range(n):
        res.append(b * pow(math.e, a * x[i]))
    return res

#Квадратичная функция
def squar(x, y):
    n = len(x)
    xy = []
    xxy = []
    sqrx = []
    cubx = []
    fourx = []
    for i in range(n):
        xy.append(x[i] * y[i])
        sqrx.append(pow((x[i]), 2))
        cubx.append(pow((x[i]), 3))
        fourx.append(pow((x[i]), 4))
        xxy.append(pow((x[i]), 2) * y[i])
    lin1 = [sum(fourx), sum(cubx), sum(sqrx)]
    lin2 = [sum(cubx), sum(sqrx), sum(x)]
    lin3 = [sum(sqrx), sum(x), n]
    vec = [sum(xxy), sum(xy), sum(y)]
    matrix = numpy.array([lin1, lin2, lin3])
    vector = numpy.array(vec)
    result0 = numpy.linalg.solve(matrix, vector)
    result = []
    for i in range(len(result0)):
        result.append(round(result0[i], 2))
    s = 0
    for i in range(n):
        s += pow(result[0] * pow(x[i], 2) + result[1] * x[i] + result[2] - y[i], 2)
    s = round(s, 2)
    pogr['погрешность квадратичной функции.'] = s
    print("\nКоэффициенты квадратичной функции: a = ", result[0], " b = ", result[1], " c = ", result[2])
    print("Погрешность квадратичной функции: ", s)
    res = []
    for i in range(n):
        res.append(result[0] * sqrx[i] + result[1] * x[i] + result[2])
    return res

#Функция для нахождения ключа словаря по его значению
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def draw():
    res1 = line(x, y)
    res2 = stepen(x, y)
    res3 = expo(x, y)
    res4 = squar(x, y)
    print("\nНаименьшей погрешностью является", get_key(pogr, min(pogr.values())))
    #print('Наилучшая погрешность', min(pogr))
    fig, ax = plt.subplots()
    plt.grid()
    ax.plot(x, y, 'p', label='Эксперементальные данные', color='black')
    ax.plot(x, res1, label='Линейная функция', color='red')
    ax.plot(x, res2, label='Степенная функция', color='green')
    ax.plot(x, res3, label='Показательная функция', color='blue')
    ax.plot(x, res4, label='Квадратичная функция', color='orange')
    ax.legend()
    fig.set_figheight(5)
    fig.set_figwidth(8)
    plt.show()
draw()



