# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

us_num_1 = int(input('Введите количество элементов 1-ого множества: '))

set_num = [int(input(f'введите {i + 1} элемент: ')) for i in range(us_num_1)]

us_num_2 = int(input('Введите количество элементов 2-ого множества: '))

set_num_2 = [int(input(f'введите {i + 1} элемент: ')) for i in range(us_num_2)]

set_num = set(set_num)
set_num_2 = set(set_num_2)

print(set_num, set_num_2)

new_set = set_num & set_num_2
print(new_set)