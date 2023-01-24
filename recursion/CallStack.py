def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

"""
output will be:
    Three
    Two
    One
"""
funcOne()

