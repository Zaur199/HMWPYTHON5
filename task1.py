# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_path(path: str) -> tuple[str]:
    return os.path.split(path)[0], *os.path.split(path)[-1].split('.')

print(split_path('/home/zaur/Learning/Data_Engineer/Deep_Python/Homework5/task1.py'))
    