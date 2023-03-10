"""
Задание 2.

Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка (Cell).
В его конструкторе инициализировать параметр (quantity),
соответствующий количеству ячеек клетки (целое число).

В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()),
вычитание (sub()),
умножение (mul()),
деление (truediv()).

Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

Пример клиентского кода:
print("Создаем объекты клеток")
cell1 = Cell(30)
cell2 = Cell(25)
cell3 = Cell(10)
cell4 = Cell(15)
print()

print("Складываем")
print(cell1 + cell2)
print()

print("Вычитаем")
print(cell2 - cell1)
print(cell4 - cell3)
print()

print("Умножаем")
print(cell2 * cell1)
print()

print("Делим")
print(cell1 / cell2)
print()


Результаты:
Создаем объекты клеток

Складываем
Сумма клеток = (55)

Вычитаем
Разность отрицательна, поэтому операция не выполняется
Разность клеток = (5)

Умножаем
Умножение клеток = (750)

Делим
Деление клеток = (1)
"""


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Сумма клеток = {self.quantity + other.quantity}'

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return f'Разность клеток = {self.quantity - other.quantity}' 
        return f'Разность отрицательна, поэтому операция не выполняется'

    def __mul__(self, other):
        return f'Умножение клеток = {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Деление клеток = {self.quantity // other.quantity}'

   
c1 = Cell(30)
c2 = Cell(25)
c3 = Cell(10)
c4 = Cell(15)
print(f'Создаём объекты клеток: {c1.quantity}, {c2.quantity}, {c3.quantity}, {c4.quantity}\n')

print('Складываем:')
print(c1 + c2)
print()

print('Вычитаем:')
print(c2 - c1)
print(c4 - c3)
print()

print('Умножаем:')
print(c2 * c1)
print()

print('Делим:')
print(c1 / c2)
print()