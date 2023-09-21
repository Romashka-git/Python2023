from data_create import *


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
          '4. Адрес\n')
    index = int(input('Введите номер варианта: ')) - 1
    search = input('Введите искомый контакт: ')
    with open('book.txt', 'r', encoding='utf-8') as data:
        # data.seek(2)
        # print(data.readlines())
        # print(data.read().split(' '))
        # print(data.readline())
        # print(data.read().strip().split('\n'))
        file = data.read().strip().split('\n')
        print(file)
        for item in file:
            new_item = item.split()
            if search in new_item[index]:
                print(item)

def change_contact():
    print('Введите номер варианта поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Номер\n'
          '4. Адрес\n')
    index = int(input('Введите номер варианта: ')) - 1
    search = input('Введите искомый контакт: ')
    search = search.capitalize()
   
    with open('book.txt', 'a+', encoding='utf-8') as data:
        data.seek(0)
        n = 0
        file = data.read().strip().split('\n')
        print('Сейчас выведу список контактов, соответствующих выборке.')
        for item in range(len(file)):
            new_item = file[item]
            new_item = new_item.split()
            if search in new_item[index]:
                data.seek(0)
                print(file[item])
                n = input('Это тот контакт? Если да, нажмите "y": ')
                if n == 'y'.lower():
                    new_obj = input('Введите новые данные:\n')
                    file[item] = file[item].replace(file[item], new_obj)
                else:
                    continue
        print('Контакты кончились')
        
    with open ('book.txt', 'w', encoding='utf-8') as data:
        tmp_file = ''
        for item in file:
            tmp_file += item + '\n'
            
        data.write(tmp_file)

def delete_contact():
    print('Введите номер варианта поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Номер\n'
          '4. Адрес\n')
    index = int(input('Введите номер варианта: ')) - 1
    search = input('Введите искомый контакт: ')
    search = search.capitalize()
   
    with open('book.txt', 'a+', encoding='utf-8') as data:
        data.seek(0)
        n = 0
        file = data.read().strip().split('\n')
        print('Сейчас выведу список контактов, соответствующих выборке.')
        for item in range(len(file)):
            new_item = file[item]
            new_item = new_item.split()
            if search in new_item[index]:
                data.seek(0)
                print(file[item])
                n = input('Это тот контакт? Если да, нажмите "y": ')
                if n == 'y'.lower():
                    new_obj = ''
                    file[item] = file[item].replace(file[item], new_obj)
                else:
                    continue
        print('Контакты кончились')
        
    with open ('book.txt', 'w', encoding='utf-8') as data:
        tmp_file = ''
        for item in file:
            tmp_file += item + '\n'
            
        data.write(tmp_file)