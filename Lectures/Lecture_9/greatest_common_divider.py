'''def gcd(a,b):
    #aлгоритм Евклида, классика. Малопроизводителен.
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a-b, b)
        else: #a < b
            return gcd(a, b-a)'''


def gcd(a,b):
    #алгоритм Евклида через остатки
    if b ==0:
        return a
    else:
        print(a,b)
        return gcd(b, a%b)

print(gcd(144, 1028))

"""
144 1028
1028 144
144 20
20 4
4
"""


'''Пояснение:
   c = a%b
   c == 0?
   Да ==> b - ответ
   Нет ==> a = c, т.е.
   a = b
   b = c
   '''
