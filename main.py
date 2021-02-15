import sys
import os
import pathlib
import os.path, time
import shutil
from prettytable import PrettyTable



def write():
    name_file = input('Введите название записи: ')
    with open((name_file + '.txt'), 'x', encoding='utf-8') as f:
        text_file = input('Введите текст: ')
        f.write(text_file)
  

def data_time():
    table = PrettyTable()
    table.field_names = ['Name', 'Date of creation', 'Last change']
    
    file_path = pathlib.Path().glob('*.txt')

    for file in file_path:
        list_files = []
        list_files.extend([file, time.ctime(os.path.getctime(file)), time.ctime(os.path.getmtime(file))])
        table.add_row([*list_files])

    print(table)

    print('Хотите прочитать запись? [Yes/No]')
    n = input('Введите ответ: ')
    if n == "yes":
        filename = input('Введите название файла, которое хотите прочитать без ".txt": ')
        with open((filename + '.txt'), 'r', encoding='utf-8') as f:
            print(*f.readlines())
    else:
        print('Тоже как вариант...')
        

def path():
    print('Текущий путь: ', os.path.abspath(__file__))
    print('Хотите сменить директорию? [Yes/No]')
    option_dir = input('Введите ответ: ')
    if option_dir == "yes":
        new_path = input('Введите новый путь: ')
        arr = os.listdir()
        for i in arr:
            print(i)
            shutil.move(i, new_path)
    else:
        print('Тоже как вариант...')
    


def blocknot(choice):
    print('Добро пожаловать! Выберите вариант: 1. Новая запись 2. Список записей 3. Настройки')
    choice = input('Введите номер: ')

    if choice == "1":
        write()
    elif choice == "2":
        data_time()
    elif choice == "3":
        path()
    else:
        print('Что-то пошло не так. Попробуйте снова...')
        sys.exit()

    while True:
        flag = input('Вернуться в начальное меню? [Yes/No]: ')
        if flag == "yes":
            blocknot(choice)
        else:
            break


if __name__=="__main__":
    choice = '' 
    blocknot(choice)
    
    