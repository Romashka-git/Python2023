# 2) (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива. 
# затем размер второго массива M  
# и элементы второго массива
# Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок последовательности сохранить исходный
# Ввод: 			Вывод:
# 7			3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

import random

list_3 = []

list_1 = [random.randint(1, 100) for i in range(7)]
list_2 = [random.randint(1, 100) for i in range(8)]
for num in list_1:
    if num not in list_2:
        list_1.append(num)


print(list_3)