# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5
#--------------------------------------------------
# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 10
# max = 0
# length = len(list_1)

# for i in range(length):
#     if (k - list_1[i]) < k - max and k - list_1[i] > 0:
#         max = list_1[i]
# print(max)  

#--------------------------------------------------  

list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
x = 10

lst = map(int, (list_1))
print(min(lst, key=lambda a:abs(a-x)))

#-------------------------------------------------- 

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

