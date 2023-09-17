# 2) - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса
# и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.

# def find_farthest_orbit(list_of_orbits):
#     pi = 3.14
#     list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
#     S = [pair[0] * pair[1] * pi for pair in list_of_orbits]
#     max_area = max(S)
#     max_area_index = S.index(max_area)
#     return list_of_orbits[max_area_index]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# x = find_farthest_orbit(orbits)
# print(x)

# def find_farthest_orbit(list_of_orbits):
#     pi = 3.14
#     # list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
#     list_of_orbits = filter(lambda x: x[0] != x[1], list_of_orbits)
#     S = [pair[0] * pair[1] * pi for pair in list_of_orbits]
#     max_area = max(S)
#     max_area_index = S.index(max_area)
#     return list_of_orbits[max_area_index]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(list_of_orbits):
    pi = 3.14
    # list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
    list_of_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    S = [pair[0] * pair[1] * pi for pair in list_of_orbits]
    max_area = max(S)
    max_area_index = S.index(max_area)
    return list_of_orbits[max_area_index]

x = find_farthest_orbit(orbits)
print(x)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# a = list(enumerate(orbits))
# print(a)