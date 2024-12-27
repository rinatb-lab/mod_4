from math import inf
def divide(first , second):
    if second == 0:
        res = inf
    else:
        res = first / second
    return res

a = divide(4 , 2)
print(a)
