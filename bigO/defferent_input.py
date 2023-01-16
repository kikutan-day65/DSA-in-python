def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

"""
in this case time complexity can be O(n + n) = O(2n) = O(n)?
-> No!! if loop has different parameters, time complexity: O(a+b)
   and cannnot be simplified anymore.
"""


# time complexity: O(a*b)
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i,j)
