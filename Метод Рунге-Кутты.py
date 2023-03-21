import math
import numpy as np
import matplotlib.pyplot as plt

#Система №1
# x' = -2x + 4y, x(0) = 3
def fun_x1(x, y):
    return -2 * x + 4 * y

# y' = -x + 3y, y(0) = 0
def fun_y1(x, y):
    return -x + 3 * y

#Система №2
# x' = y, x(0) = 2
def fun_x2(x, y):
    return y

# y' = 2y, y(0) = 2
def fun_y2(x, y):
    return 2 * y

#Точное значение №1
def exact_x1(t):
    return 4 * math.exp(-t) - math.exp(2 * t)

def exact_y1(t):
    return math.exp(-t) - math.exp(2 * t)

#Точное значение №2
def exact_x2(t):
    return math.exp(2 * t) + 1

def exact_y2(t):
    return 2 * math.exp(2 * t)

# Подсчет коэффициетов для двух фкункций
def coef(fun_x, fun_y, x, y, h):

    k1 = h * fun_x(x, y)
    l1 = h * fun_y(x, y)

    k2 = h * fun_x(x + k1 / 2.0, y + l1 / 2.0)
    l2 = h * fun_y(x + k1 / 2.0, y + l1 / 2.0)

    k3 = h * fun_x(x + k2 / 2.0, y + l2 / 2.0)
    l3 = h * fun_y(x + k2 / 2.0, y + l2 / 2.0)

    k4 = h * fun_x(x + k3, y + l3)
    l4 = h * fun_y(x + k3, y + l3)

    d_x = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
    d_y = (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0
    return d_x, d_y

def runge_kutta(fun_x, fun_y, x0, y0, t_f, h, t0):
    x = [x0]
    y = [y0]
    t = [t0]
    for i in range(t_f):
        d_x, d_y = coef(fun_x, fun_y, x0, y0, h)
        x0 = x0 + d_x
        y0 = y0 + d_y
        t0 = t0 + h
        x.append(x0)
        y.append(y0)
        t.append(t0)
    return x, y, t

#отрисовка точного решения
def exact_solution(exact_x, exact_y, t0, t_f):
    N = 100
    x, y = [], []
    t = np.linspace(t0, t_f, N)
    for i in t:
        x.append(exact_x(i))
        y.append(exact_y(i))
    return x, y, t



def make_chart(fun_x, fun_y, exact_x, exact_y, x0, y0, t0, t_f, h, title):
    x, y, t = runge_kutta(fun_x, fun_y, x0, y0, t_f, h, t0)
    x1, y1, t1 = exact_solution(exact_x, exact_y, t0, h * t_f)
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(t1, x1, label='Точное решение для x(t)')
    ax.plot(t1, y1, label='Точное решение для y(t)')
    ax.plot(t, x, label='Метод Рунге-Кутта для x(t)')
    ax.plot(t, y, label='Метод Рунге-Кутта для y(t)')
    ax.legend()
    fig.set_figwidth(8)
    fig.set_figheight(5)
    plt.title(title)
    plt.show()

t_f = 5
h = 0.1
make_chart(fun_x1, fun_y1, exact_x1, exact_y1, 3, 0, 0, t_f, h, "Пример №1")
make_chart(fun_x2, fun_y2, exact_x2, exact_y2, 2, 2, 0, t_f, h, "Пример №2")

