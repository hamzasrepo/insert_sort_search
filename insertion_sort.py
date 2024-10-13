# insertion_sort.py - Sorts an unsorted list via insertion
from insertion import insert_cabinet

def insertion_sort(cabinet):
    new_cabinet = []
    #file = len(cabinet) - 1
    while len(cabinet) > 0:
       to_insert = cabinet.pop()
       new_cabinet = insert_cabinet(new_cabinet, to_insert)
       #file -= 1
    '''for file in cabinet.copy():
       to_insert = cabinet.pop()
       new_cabinet = insert_cabinet(new_cabinet, to_insert)'''
    return new_cabinet

cabinet = [8, 4, 6, 1, 2, 5, 3, 7]
sorted_cabinet = insertion_sort(cabinet)
print(sorted_cabinet)   