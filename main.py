import sys
import os
import pathlib
import os.path, time
import codecs
import shutil


def write():
    name_file = input('Введите название записи: ')
    with codecs.open((name_file + '.txt'), 'x', encoding='utf-8') as f:
        text_file = input('Введите текст: ')
        f.write(text_file)
  

def data_time():
    file_path = pathlib.Path().glob('*.txt')
    for file in file_path:
        list_files = []
        list_files.extend([file, time.ctime(os.path.getctime(file)), time.ctime(os.path.getmtime(file))])
        print(*list_files)
    print('Хотите прочитать запись? [Да/Нет]')
    n = input('Введите ответ: ')
    if n == "да":
        filename = input('Введите название файла, которое хотите прочитать без ".txt": ')
        with codecs.open((filename + '.txt'), 'r', encoding='utf-8') as f:
            print(*f.readlines())
    else:
        print('Тоже как вариант...')
        

def path():
    print('Выберите вариант: 1. Сменить путь 2. Удалить все записи')
    number_dir = input('Введите номер: ')
    if number_dir == "1":
        print('Текущий путь: ', os.path.abspath(__file__))
        print('Хотите сменить директорию? [Да/Нет]')
        option_dir = input('Введите ответ: ')
        if option_dir == "да":
            new_path = input('Введите новый путь: ')
            arr = os.listdir()
            for i in arr:
                print(i)
                shutil.move(i, new_path)
        else:
            print('Тоже как вариант...')
    elif number_dir == "2": # не работает
        k = os.path.abspath(__file__)
        filelist = [ f for f in k if f.endswith(".txt") ]
        for f in filelist:
            os.remove(os.path.join(k, f))
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
        flag = input('Вернуться в начальное меню? [Да/Нет]: ')
        if flag == "да":
            blocknot(choice)
        else:
            break


if __name__=="__main__":
    choice = '' 
    blocknot(choice)
    
    