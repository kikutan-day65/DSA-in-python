num1 = 11

num2 = num1

print("before num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
if id(num1) == id(num2):
    print("both points to the same memory!\n")
else:
    print("both points to the different memory!")


num2 = 22

print("after num2 value is updated: ")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
if id(num1) == id(num2):
    print("both points to the same memory!")
else:
    print("both points to the different memory!")

print("------------------------------------------------")


dict1 = {
    'value': 11,
    'next' : 12
}

dict2 = dict1

print("before dict2 value is updated: ")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
if id(dict1) == id(dict2):
    print("both points to the same memory!\n")
else:
    print("both points to the different memory!")


dict2['value'] = 22

print("after dict2 value is updated: ")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
if id(dict1) == id(dict2):
    print("both points to the same memory!")
else:
    print("both points to the different memory!")