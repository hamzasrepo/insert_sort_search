import math

def binary_search(cabinet, looking_for):
    lower_bound = 0
    upper_bound = len(cabinet) - 1
    
    while lower_bound <= upper_bound:
        guess = math.floor((upper_bound + lower_bound) / 2)
        if looking_for > cabinet[guess]:
            lower_bound = guess + 1
        elif looking_for < cabinet[guess]:
            upper_bound = guess - 1
        else:
            break
    
    return guess

sorted_cabinet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(sorted_cabinet, 6))
