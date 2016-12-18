def choice_sort(A):
    '''
    После i итераций срез A[0:i] содержит эл-ты A, стоящие на окончательных позициях.
    N-1 итерация
    O(N**2)
    '''
    for i in range(1, len(A)): #i - номер итерации,
        for k in range(i, len(A)): #полагаем i-тый эл-т временным минимумом в цикле
            if A[k] < A[i-1]:
                A[k], A[i-1] = A[i-1], A[k]

from test_list import *


print(choice_sort(A))
"""
[3, 6, 5, 2, 4, 1]
[2, 6, 5, 3, 4, 1]
[1, 6, 5, 3, 4, 2]
[1, 5, 6, 3, 4, 2]
[1, 3, 6, 5, 4, 2]
[1, 2, 6, 5, 4, 3]
[1, 2, 5, 6, 4, 3]
[1, 2, 4, 6, 5, 3]
[1, 2, 3, 6, 5, 4]
[1, 2, 3, 5, 6, 4]
[1, 2, 3, 4, 6, 5]
[1, 2, 3, 4, 5, 6]
"""

#второй вариант записи этой сортировки:

def choice_sort(A):
    for pos in range(0, len(A)-1): #pos - позиция временного минимума
        for k in range(pos+1, len(A)):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]