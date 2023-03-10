"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы. [[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() 
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str('\n'.join('\t'.join([str(el) for el in i]) for i in self.lst))

    def __add__(self, other):
        for i in range(len(self.lst)):
            for j in range(len(other.lst[i])):
                self.lst[i][j] = self.lst[i][j] + other.lst[i][j]
        return Matrix(self.lst)


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'{m_1}\n')
print(f'{m_2}\n')
print(f'Сумма матриц:\n{m_1+m_2}')