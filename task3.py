"""
Задание 3.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя 
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):

    def __init__(self, text):
        self.text = text


def division_by_zero(a, b):

    try:
        if b == 0:
            raise OwnError("Деление на ноль невозможно")
    except OwnError as err:
        print(err)
    else:
        print(f'Частное = {a / b}')


divider = int(input("Введите делимое: "))
denominator = int(input("Введите делитель: "))

division_by_zero(divider, denominator)
