phone_book = 'phone_book.txt'


def all_contacts():
    print('В справочнике содержаться следующие контакты:')
    with open(phone_book, 'r', encoding='utf8') as book:
        for line in book:
            print(line.replace("\r", "").replace("\n", ""))


def search_contact(contact):
    with open(phone_book, 'r', encoding='utf8') as book:
        count = 0
        for line in book:
            if contact in line:
                print(line.replace("\r", "").replace("\n", ""))
                count = +1
        if count == 0:
            print('Нет данных, удовлетворяющих введенным значениям!')


def add_contact(contact):
    with open(phone_book, 'a', encoding='utf8') as book:
        book.write('\n' + contact)
    print('Контакт успешно добавлен в справочник!')


def delete_contact(contact):
    with open(phone_book, 'r', encoding='utf8') as book:
        lines = book.readlines()
    with open(phone_book, 'w', encoding='utf8') as book:
        count = 0
        for line in lines:
            if contact in line:
                count = +1
            else:
                book.write(line)
        if count == 0:
            print('Нет данных, удовлетворяющих введенным значениям!')
        else:
            print("Запись в телефонном справочнике удалена!")


def change_contact(name, new_name):
    with open(phone_book, 'r', encoding='utf8') as book:
        x = book.read()
    with open(phone_book, 'w', encoding='utf8') as book:
        x = x.replace(name, new_name)
        book.write(x)
    print("Данные изменены")


def main_menu():
    while True:
        numb = int(input(f'Введите:\n'
                         '1 - для просмотра справочника,\n'
                         '2 - для поиска контакта, \n'
                         '3 - для добавления контакта,\n'
                         '4 - для изменения данных,\n'
                         '5 - для удаления контакта,\n'
                         '6 - для выхода из справочника:\n'))
        while (numb < 1) or (numb > 6):
            numb = int(input('Введите значение от 1 до 6: '))
        if numb == 1:
            all_contacts()
        elif numb == 2:
            search_contact(
                input('Введите искомое фамилию/имя/отчество/номер телефона:'))
        elif numb == 3:
            add_contact(
                input('Для добавления нового пользователя введите ФИО и номер телефона:'))
        elif numb == 4:
            change_contact(input('Введите, что вы хотите изменить: '),
                           input('На что необходимо изменить:'))
        elif numb == 5:
            delete_contact(input(
                'Введите фамилию/имя/отчество/номер телефона для удаления данного контакта:'))
        elif numb == 6:
            break

main_menu()
