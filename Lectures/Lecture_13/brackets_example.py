'''Структуры данных делятся на два вида
по характеру хранения данных и по интерфейсу доступа к ним'''

'''Стек - это LIFO-очередь'''
'''Очередь - это FIFO-очередь'''

from class_LinkedList import *
def correct_braces_sequence(expression):
    stack = LinkedList()
    left = ['(','[','{']
    right = [')',']','}']
    other_brace = dict(zip(left,right)) #сопоставление левой и правой скобок
    for brace in expression:
        if brace in left:
            stack.push_front(brace)
        elif brace in right:
            if stack.empty(): #если первая встреченная скобка - правая
                return False
            if brace != other_brace(stack.pop()):
                return False
    return stack.empty() #если все скобки совпали, результат будет зависеть от наличия лишних скобок в стеке

print(correct_braces_sequence('()()(((())'))



