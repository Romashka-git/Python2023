# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны 
# находиться  в файле.
# 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def input_firstname():
    return input('Введите имя: ').title()

def input_lastname():
    return input('Введите Фамилию: ').title()

def input_phone():
    return input('Введите номер абонента: ')

def input_adress():
    return input('Введите адрес абонента: ').capitalize()

def input_data(msg='Введите данные абонента'):
    print(msg)
    name = input_firstname()
    lastname = input_lastname()
    phone = input_phone()
    adress = input_adress()
    # return name, lastname, phone, adress
    with open('book.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {lastname} {phone} {adress} \n')

def print_data():
    with open('book.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search_contact():
    print('Введите варианты поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Номер\n'
          '4. Телефон\n')
    index = int(input('Введите номер варианта: ')) - 1
    search = input('Введите искомый контакт: ')
    with open('book.txt', 'r', encoding='utf-8') as data:
        # print([data.read()])
        # data.seek(2)
        # print(data.readlines())
        # print(data.read().split(' '))
        # print(data.readline())
        
        # print(data.read().strip().split('\n'))
        file = data.read().strip().split('\n')
        for item in file:
            # print(item.split())
            new_item = item.split()
            if search in new_item[index]:
                print(item)

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


interface()