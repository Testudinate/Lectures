def fib(n):
    '''
    O(Fib_n) - это плохой алгоритм, так как рекурсия идёт по каждой ветке дерева, и вдобавок вычисленные числа
    стираются вместе с пространствами имён каждого вызова функции
    '''
    assert n >= 0
    if n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2) #здесь оба вычитания вып. на прямом ходу рекурсии, а сложение - на обратном

    '''Отсюда мораль: осторожно с рекурсией там, где в функции есть больше одного вызова подзадачи'''

print(fib(13))