import numpy as np

#Поступление заданий на станок (экспоненциальное распределение)
def get_time_before_next_task():
    return round(np.random.exponential(1.0), 2)

#Наладка станка (равномерное распределение)
def setting_machine():
    return round(np.random.uniform(0.1, 0.5), 2)

#Время выполнения задания (нормальное распределение)
def get_task_execution():
    return round(np.random.normal(0.5, 0.1), 2)

#Время ожидания поломки
def time_before_machine_break():
    return round(np.random.normal(20.0, 2.0), 2)

#Время починки
def get_repair_time():
    return round(np.random.uniform(0.1, 0.5), 2)

def machine_work(tasks):
    total_work_time = 0
    details = tasks
    kol_brok = 0
    total_repair_time = 0
    time_before_next_task = get_time_before_next_task()
    time_to_broke = time_before_machine_break()
    while details > 0:
        if time_before_next_task > 0:
            total_work_time += time_before_next_task
            time_before_next_task = 0

        set_machine = setting_machine()
        task_execution = get_task_execution()
        time_one_task = set_machine + task_execution

        if time_one_task < time_to_broke:
            time_before_next_task += get_time_before_next_task()
            total_work_time += time_one_task
            time_to_broke -= time_one_task
            time_before_next_task -= time_one_task
            details -= 1
        else:
            kol_brok += 1
            total_work_time += time_to_broke
            time_before_next_task -= time_to_broke
            repair_time = get_repair_time()
            total_work_time += repair_time
            time_before_next_task -= repair_time
            time_to_broke = time_before_machine_break()
            total_repair_time += repair_time

    while time_before_next_task < 0:
        time_before_next_task += get_time_before_next_task()
    return kol_brok, total_work_time, total_repair_time


tasks = 500
res = machine_work(tasks)

print("Количество заданий:", tasks)
print("Количество поломок станка:", res[0])
print("Время работы", int(res[1]), "часов", int(res[1] % 1 * 60), "минут")
print("Время починки:", int(res[2]), "часов", int(res[2] % 1 * 60), "минут")
