import math
import matplotlib.pyplot as plt
import numpy as np

#Метод серединных квадратов
def square_method(num, n):
    Endlist = []
    for i in range(n):
        num2 = pow(num, 2)
        print(num2)
        count1 = len(str(num))
        count2 = len(str(num2))
        num3 = ""
        for i in range(count2):
            if (i < count1 / 2):
                num2 //= 10
            elif (i >= count1 / 2 and i < count1 / 2 + count1):
                num3 += str(num2 % 10)
                num2 //= 10
        if(num3 == ''):
            break
        count3 = len(num3)
        num3_1 = int(num3[::-1])
        num4 = pow(10, -count3)
        num = num3_1
        Endlist.append(num3_1 * num4)
    return Endlist

# Метод произведений
def product_method(num, core, n):
    Endlist = []
    for i in range(n):
        num2 = num * core
        num2_1 = num2
        num3 = ""
        step = 0
        step2 = 0
        count1 = len(str(num))
        count2 = len(str(num2))
        for i in range(count2):
            if (i < count1 / 2):
                num2 //= 10
            elif (i >= count1 / 2 and i < count1 / 2 + count1):
                num3 += str(num2 % 10)
                step += 1
                num2 //= 10
        num3_1 = int(num3[::-1])
        count4 = len(num3)
        num4 = pow(10, -count4)
        Endlist.append(num3_1 * num4)
        for i in range(count2):
            if (i < count2 / 2):
                num4 += num2_1 % 10 * pow(10, step2)
                step2 += 1
                num2_1 //= 10
        num = round(num4)
    return Endlist

# Смешанный конгруэнтный метод
def mix_congruent_method(num, mult, a, m, n):
    Endlist = []
    for i in range(n):
        num2 = (num * mult + a) % m
        count = len(str(num2))
        count2 = pow(10, -count)
        Endlist.append(num2 * count2)
        mult = num2
    return Endlist

# Мультипликативный конгруентный метод
def mult_congruent_method(num, mult, m, n):
    Endlist = []
    for i in range(n):
        num2 = (num * mult) % m
        count = len(str(num2))
        count2 = pow(10, -count)
        Endlist.append(num2 * count2)
        mult = num2
    return Endlist

def draw(res, title, c):
    plt.grid()
    plt.title(title)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.hist(res, color=c, bins=np.arange(0, 1.1, step=0.1))
    plt.show()

res1 = square_method(7153, 500)
draw(res1, 'Метод серединных квадратов', 'red')

res2 = product_method(3729, 5167, 500)
draw(res2, 'Метод произведений', 'green')

res3 = mix_congruent_method(1357, 1357, 1, 5689, 500)
draw(res3, 'Смешанный конгруентный метод', 'blue')

res4 = mult_congruent_method(1357, 1357, 5689, 20)
draw(res4, 'Мультипликативный конгруентный метод', 'yellow')
