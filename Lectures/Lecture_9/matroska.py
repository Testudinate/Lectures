def matroska(n):
    if n ==1: #крайний случай
        print('матрёшечка')
    else:
        print('верх матрёшки')
        matroska(n-1)
        print('низ матрёшки')

matroska(5)
"""
верх матрёшки
верх матрёшки
верх матрёшки
верх матрёшки
матрёшечка
низ матрёшки
низ матрёшки
низ матрёшки
низ матрёшки
"""