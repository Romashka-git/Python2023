# Напишите функцию same_by(characteristic, objects), которая проверяет, 
# все ли объекты имеют одинаковое значение некоторой характеристики, 
# и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
# Ввод:							Вывод:
# values = [0, 2, 10, 6]		same
# if same_by(lambda x: x % 2, values):
# 	print(‘same’)
# else:
# 	print(‘different’)

# def same_by(characteristic, objects):
# 	list1 = list(map(characteristic, objects))
# 	print(list1)
# 	for i in range(len(list1)):
# 		if list1[i] == False:
# 			return False
# 	return True
	
def same_by(characteristic, objects):
    result_list = list(filter(characteristic, objects))
    print(result_list)

    if objects == result_list or result_list == []:
        return True
    return False



values = [1, 3, 5, 7]

if same_by(lambda x: x % 2, values):
	print('same')
else:
	print('different')
      