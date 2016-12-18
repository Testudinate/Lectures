A = [1,2,3]
def f(B):
    B = B + ['n']
    # Ошибка вылезет без return B?
print(f(A))