#Инкапсуляция этой ссылки в собственный тип:
class LinkedList:
        
    def __init__(self):
            self._A = None

    def __str__(self):
        p = self._A
        while p:  # !=None
            print(p[0])
            p = p[1]

    def empty(self):
        return not self._A

    def push_front(self, data):
        p = [data, self] #вставка данных в начало списка
        self = p

    def pop_front(self): #удаляет эл-т из списка и возвращает его data
        if self.empty:
            raise IndexError()
        data = self._A[0]
        self._A = self._A[1]
        return data






