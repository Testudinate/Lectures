def pow(a, n):
    #это просто возведение в степень
    if n ==0:
        return 1
    else:
        return pow(a, n-1)*a

'''Оптимизация процесса сокращения степени:
Если а - чётная, то (a**2)**(n/2)'''

def fastpow(a, n):
    if n ==0: #крайний случай
        return 1
    elif n%2 ==0:
        return fastpow(a*a, n//2)
    else:
        return fastpow(a, n-1)*a

print(fastpow(6,7))