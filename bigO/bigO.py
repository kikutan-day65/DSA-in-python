"""
time complexity notations:
    O(n^2)
    O(n*log(n))
    O(log(n))
    O(1)

O(n^2) >>>> O(n*log(n)) >>>> O(log(n)) >>>> O(1)
"""


# time complexity: O(n)
def print_items(n):
    for i in range(n):
        print(i, end=" ")

print_items(10)
print()


# What if there're two for loops in the function?
def print_nums(n):
    for i in range(n):
        print(i, end=" ")
    print()
    for j in range(n):
        print(j, end=" ")

print_nums(10)
print()

"""
in this case time complexity: O(n+n) = O(2n)
however, we can simplifiy it to remove the constant.
thus, time complexity: O(n) as well as function above.
"""


# what if there's a nested loop?
def nest_print_num(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

nest_print_num(10)
print()

"""
in this case tmie complexity: O(n*n) = O(n^2)
"""


# drop non-determinants
def print_items2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    for k in range(n):
        print(k)

print_items2(10)
print()

"""
in this case, time complexity: O(n^2) + O(n) = O(n^2+n)
because of n^2 >>>>>>>>>>> n, we can remove n in the O(n^2+n)
thus, time complexity: O(n^2)
"""


# time complexity: O(1) = constant time
def add_items(n):
    return n + n
