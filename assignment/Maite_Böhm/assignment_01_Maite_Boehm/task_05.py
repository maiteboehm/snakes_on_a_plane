# assignment 1
# Task 05 - Triangle Checking

# start of code
print("Please input a:")
a = int(input())
# a = 4
values = []
values.append(a)

print("Please input b:")
b = int(input())
# b = 4
values.append(b)

print("Please input c:")
c = int(input())
# c = 4
values.append(c)
values.sort()

if values[2] < (values[0] + values[1]):
    if values[0] == values[1]:
        if values[1] == values[2]:
            print("equilateral triangle")
        else:
            print("isosceles triangle")
    else:
        if values[1] == values[2]:
            print("isosceles triangle")
        else:
            print("scalene triangle")
else:
    print("No valid triangle. Please input new values.")
