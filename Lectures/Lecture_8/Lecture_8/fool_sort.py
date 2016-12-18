def fool_sort(A):
    '''
    После i итераций i эл-тов в конце стоят на своих местах.
    N-1 итерация
    O(N**3)
    '''
    i = 0
    while i < len(A):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            i = 0 #сброс текущей позиции
        else:
            i+=1

from test_list import *

fool_sort(A)
print(A)