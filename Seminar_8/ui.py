from logger import *

def interface():
    print('Выберете действия:\n'
          '1. Добавить контакт\n'
          '2. Вывести контакты\n'
          '3. Поиск контактов\n'
          '4. Выход\n')
    cmd = input('Введите номер действия ')
    while cmd not in ('1', '2', '3', '4'):
        print('Некорректно')
        cmd = cmd = input('Введите номер действия')
    match cmd:
        case '1': input_data()
        case '2': print_data()
        case '3': search_contact()
        case '4': exit