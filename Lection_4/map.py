# def where(f, col):
#     return [x for x in col if f(x)]

list_1 = [i for i in range(1, 11)]
print(list_1)

list_1 = list(map(lambda x: x ** 2, list_1))
print(list_1)

# C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

a = '4 5 6 7 7 5'
a = a.split()
print(*a)

a = list(map(int, a))
print(a)