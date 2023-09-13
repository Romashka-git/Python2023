# В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# list = [1, 2, 3, 5, 8, 15, 23, 38]

# def math (op):
#     l = [i for i in op if i % 2 == 0]
#     l_2 = [(i, i * i) for i in l]
#     return l_2

# l_res = math(list)
# print(l_res)

def select(f, col):    #map
    return [f(x) for x in col]

def where(f, col):    #filter
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)

res = where(lambda x: x % 2 == 0, res)
print(res)