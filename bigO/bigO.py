
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

"""
in this case time complexity: O(n+n) = O(2n)
however, we can simplifiy it to remove the constant.
thus, time complexity: O(n) as well as function above.
"""
