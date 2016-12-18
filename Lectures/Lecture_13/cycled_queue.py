A = [10, [20, [30, None]]]
A[1][1][1] = A #зацикливание списка
def print_list(A):
    p = A
    while p: #!=None
        print(p[0])
        p = p[1]
print_list(A)
