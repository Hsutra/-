import sys
import random
from random import randint

num = int(input("Выберите действие: \n1. Ввести значения с клавиатуры. \n2. Запустить контрольные значения. \n"))
if num == 1:
    kol_tasks = int(input('Количество заданий: '))
    b0, a0 = map(int, input('Интервалы поступления заданий в систему: ').split())
    p1, p2, p3 = map(float, input('Вероятности попадания задания на 1, 2 и 3 ЭВМ: ').split())
    p_evm_1_to_2, p_evm_1_to_3 = map(float, input('Вероятности попадания из ЭВМ 1 в ЭВМ 2 и ЭВМ 3: ').split())
    b1, a1 = map(int, input('Время выполнения задания на ЭВМ 1: ').split())
    b2, a2 = map(int, input('Время выполнения задания на ЭВМ 2: ').split())
    b3, a3 = map(int, input('Время выполнения задания на ЭВМ 3: ').split())
elif num == 2:
    kol_tasks = 200
    p1 = 0.4
    p2 = 0.3
    p3 = 0.3
    p_evm_1_to_2 = 0.3
    p_evm_1_to_3 = 0.7
    a0, b0 = 1, 3
    a1, b1 = 1, 4
    a2, b2 = 1, 3
    a3, b3 = 2, 5
else:
    print("Вы неправы!")
    sys.exit()

def add_task(task, now_time, min_time, max_time):
    time_work = randint(min_time, max_time)
    if len(task) == 0:
        task.append([time_work, now_time])
    else:
        task.append([time_work, now_time])
    return task

def del_task(task, now_time):
    task.pop(0)
    if len(task) == 0:
        return task
    else:
        task[0] = [task[0][0], now_time]
        return task
def task_wait_time(task):
    res = [0, 0, 0]
    if(task[0][0] != 0):
        res[0] = int(task[0][0] / task[0][1])

    if (task[1][0] != 0):
        res[1] = int(task[1][0] / task[1][1])

    if (task[2][0] != 0):
        res[2] = int(task[2][0] / task[2][1])

    return res

def machine():
    #время работы
    next_task_min, next_task_max = b0 - a0, b0 + a0
    evm_1_min, evm1_max = b1 - a1, b1 + a1
    evm_2_min, evm_2_max = b2 - a2, b2 + a2
    evm_3_min, evm_3_max = b3 - a3, b3 + a3
    # счётчики
    now_time = 0
    new_task_time = 0
    last_task_time = 0
    evm_1 = []
    evm_2 = []
    evm_3 = []
    evm_1_task_complete = 0
    evm_2_task_complete = 0
    evm_3_task_complete = 0
    queue = [0, 0, 0]
    task_wait = [[0, 0], [0, 0], [0, 0]]
    task_number = 0
    completed_tasks = 0
    while completed_tasks < kol_tasks:
        if now_time - last_task_time == new_task_time:
            task_number += 1
            last_task_time = now_time
            new_task_time = randint(next_task_min, next_task_max)
            new_task = random.choices((1, 2, 3), weights=[p1, p2, p3])
            if new_task == [1]:
                evm_1 = add_task(evm_1, now_time, evm_1_min, evm1_max)
            elif new_task == [2]:
                evm_2 = add_task(evm_2, now_time, evm_2_min, evm_2_max)
            else:
                evm_3 = add_task(evm_3, now_time, evm_3_min, evm_3_max)
        # Задача поступает на ЭВМ 1
        if len(evm_1) != 0:
            if now_time - evm_1[0][1] == evm_1[0][0]:
                if len(evm_1) > 1:
                    task_wait[0][0] += now_time - evm_1[1][1]
                    task_wait[0][1] += 1
                evm_1 = del_task(evm_1, now_time)
                evm_1_task_complete += 1
                # Передаем задачу на следующую ЭВМ
                rand = random.choices((1, 2), weights=[p_evm_1_to_2, p_evm_1_to_3])
                if(rand == [1]):
                    evm_2 = add_task(evm_2, now_time, evm_2_min, evm_2_max)
                else:
                    evm_3 = add_task(evm_3, now_time, evm_3_min, evm_3_max)
        else:
            queue[0] += 1
        # задача поступила на ЭВМ 2
        if len(evm_2) != 0:
            if len(evm_2) > 1:
                task_wait[1][0] += now_time - evm_2[1][1]
                task_wait[1][1] += 1
            if now_time - evm_2[0][1] == evm_2[0][0]:
                evm_2 = del_task(evm_2, now_time)
                evm_2_task_complete +=1
                completed_tasks += 1
        else:
            queue[1] += 1
        # задача поступила на ЭВМ 3
        if len(evm_3) != 0:
            if now_time - evm_3[0][1] == evm_3[0][0]:
                if len(evm_3) > 1:
                    task_wait[2][0] += now_time - evm_3[1][1]
                    task_wait[2][1] += 1
                evm_3 = del_task(evm_3, now_time)
                evm_3_task_complete += 1
                completed_tasks += 1
        else:
            queue[2] += 1
        now_time += 1

    avg_task_wait = task_wait_time(task_wait)
    # task_compl_time = [(now_time - time_no_queue[0]) / evm_1_task_complete, (now_time - time_no_queue[1]) / evm_2_task_complete, (now_time - time_no_queue[2]) / evm_3_task_complete]
    return [now_time, len(evm_1), len(evm_2), len(evm_3), now_time - queue[0], now_time - queue[1], now_time - queue[2], evm_1_task_complete, evm_2_task_complete, evm_3_task_complete,
            queue[0], queue[1], queue[2], avg_task_wait[0], avg_task_wait[1], avg_task_wait[2]]#task_compl_time[0] + (task_compl_time[1] * p_evm_1_to_2 + task_compl_time[2] * p_evm_1_to_3), task_compl_time[1], task_compl_time[2]]

a = 0

data = machine()
queue1, queue2, queue3 = data[1], data[2], data[3]
time_in_queue1, time_in_queue2, time_in_queue3, = data[13], data[14], data[15]
stop_perc_1 = round(100 * data[10] / data[0], 2)
stop_perc_2 = round(100 * data[11] / data[0], 2)
stop_perc_3 = round(100 * data[12] / data[0], 2)
stop_perc = round((stop_perc_1 + stop_perc_2 + stop_perc_3) / 3, 2)
A = 1 / b1 + 1 / b2 + 1 / b3
avg_work_time = (data[4] / data[7] + data[5] / data[8] + data[6] / data[9]) / 3
time_in_system = avg_work_time + (time_in_queue1 + time_in_queue2 + time_in_queue3) / 3

print('\nИтоги работы ЭВМ 1:')
print('Количество поступивших заданий:', data[7])
print('Общее время работы:', data[4] // 60, 'ч.', data[4] % 60, 'мин.')
print('Процент простоя:', stop_perc_1, '%')
print('Очередь:', queue1)
print('Среднее время ожидания в очереди:', time_in_queue1, 'мин.')

print('\nИтоги работы ЭВМ 2:')
print('Количество поступивших заданий:', data[8])
print('Общее время работы:', data[5] // 60, 'ч.', data[5] % 60, 'мин.')
print('Процент простоя:', stop_perc_2, '%')
print('Очередь:', queue2)
print('Среднее время ожидания в очереди:', time_in_queue2, 'мин.')

print('\nИтоги работы ЭВМ 3:')
print('Количество поступивших заданий:', data[9])
print('Общее время работы:', data[6] // 60, 'ч.', data[6] % 60, 'мин.')
print('Процент простоя:', stop_perc_3, '%')
print('Очередь:', queue3)
print('Среднее время ожидания в очереди:', time_in_queue3, 'мин.')

print("\nОбщие итоги работы системы:")
print('Общее время работы системы:', data[0] // 60, 'ч.', data[0] % 60, 'мин.')
print('Среднее время выпонения задачи:', round(avg_work_time, 2), 'мин.')
print('Среднее число каналов под обслуживанием:', round((data[4] + data[5] + data[6]) / data[0], 2))
print('Средний процент простоя:', stop_perc, '%')
print('Абсолютная пропускная способность:', round(A, 2))
print('Среднее время ожидания заявки в очереди', round((data[13] + data[14] + data[15]) / 3, 2), 'мин.')
print('Среднее время пребывания заявки в системе:', round(time_in_system, 2), 'мин.')
