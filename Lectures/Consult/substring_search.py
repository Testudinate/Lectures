'Алгоритм поиска подстроки в строке, O(N*M)'
s = 'ababccabbcaabc' #len(s) = 14
subs = 'abbc' #len(subs) = 4
def find(s, subs): #поиск подстроки в строке
    for k in range(len(s) - len(subs)):
        for i in range(len(subs)):
            if s[k+i] != subs[i]:
                break
            else:
                return k


