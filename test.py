# coding : utf-8

# Комментарий

import os
import pip
import sys
import psutil
import shutil


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)  # копируй, от куда и куда
        if os.path.exists(newfile):
            print("Файл", newfile, "был успешно создан")
            return True
        else:
            print("Возникли проблемы с копированием")
            return False

def sys_info():
    print("Вот что я знаю о системе:")
    print("Количество процессов:", pip)
    print("Платформа:", sys.platform)
    print("Кодировка файловой системы:", sys.getfilesystemencoding())
    print("Текущая директория:", os.getcwd())
    print("Текущая пользователь:", os.getlogin())

def delet_dupli():
    file_list = os.listdir(dir_name)
    # i = 0
    # while i < len(file_list):
    for f in file_list:
        fullname = os.path.join(dir_name, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
        # i += 1
        return True


print("Great Python Program!")
print("Привет, програмист!")
name = input("Ваше имя:")
print(name, "Добро пожаловать в мир Python!")

n = ''
while n != 'Q':
    n = input("\nВыбери действие: \nY-начать работу \nN-завершить работу \nQ-неизвестный ответ \n")
    if n == "Y":
        print("Отлично! Давай поработаем.")
        print(
            """
        Вот что я могу: 
        1- Запустить список файлов
        2- Запустить информацию о системе 
        3- Запустить список процессов
        4- Продублировать файлы в текущей директории
        5- Продублировать указанный файл
        6- Удалить дубликаты файлов
        """
        )
        choice = input("Выбери дейтвие из списка:")
        if choice == "1":
            print(os.listdir())
        elif choice == "2":
          sys_info()
        elif choice == "3":
            print("Запуск списка процессов:", psutil.pids())
        elif choice == "4":
            print("==Дублирование файлов в текущей директории==")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif choice == "5":
            print("Продублирую файл")
            filename = input("Ввидите имя файла, а я его продублирую:")
            duplicate_file(filename)
        elif choice == "6":
            print("Удаление дубликотав в директории")
            dir_name = input("Укажити имя директории:")
            delet_dupli()
    elif n == "N":
        print("До свидания!")
        break
    else:
        print("Неизвестный ответ")
        break
