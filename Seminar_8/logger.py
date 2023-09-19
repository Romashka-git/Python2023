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