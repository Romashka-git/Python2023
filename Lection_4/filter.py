list1 = [i for i in range(11)]
print(list1)

list1 = list(map(lambda x: x ** 2, list1))
print(list1)

# list1 = list(map(lambda x: x % 2 == 0, list1))
# print(list1)

list1 = list(filter(lambda x: x % 2 == 0, list1))
print(list1)