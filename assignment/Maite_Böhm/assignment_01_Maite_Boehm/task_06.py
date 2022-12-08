# assignment 1
# Task 06 - Decimal to Octal Conversion

# start of code
print("Please input number (integer):")
input_number = int(input())
octal_number = []

while (input_number != 0):
    octal_number.append(str(input_number % 8))
    input_number = int(input_number / 8)

octal_number.reverse()
print("".join(octal_number))

# start part b

print("Please input number (non-negative float):")
input_whole, input_dec = str(input()).split(".")
input_whole = int(input_whole)
input_dec = float("0." + input_dec)

octal_number_whole = []
octal_number_dec = []

# converting integer part into octal
while (input_whole != 0):
    octal_number_whole.append(str(input_whole % 8))
    input_whole = int(input_whole / 8)

# converting decimal into octal
for x in range(20):
    whole, dec = str(input_dec * 8).split(".")
    input_dec = float("0." + dec)
    octal_number_dec.append(whole)


octal_number_whole.reverse()
print("".join(octal_number_whole) + "." + "".join(octal_number_dec))
