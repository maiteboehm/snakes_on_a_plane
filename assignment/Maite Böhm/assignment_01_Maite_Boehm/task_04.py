# assignment 1
# Task 04 - selective printing

# start of code

import numpy as np

print("Please input number:")
input_number = int(input())
liste = np.arange(0, input_number, 1)
output = [0]

for n in liste:
    if n%3 == 0:
        continue
    else:
        output.append(n)
print(output)
