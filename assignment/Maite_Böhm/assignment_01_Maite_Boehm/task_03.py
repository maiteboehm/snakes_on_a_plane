# assignment 1
# Task 03 - Fibonacci Numbers

# start of code

print("Please, input number")
input_number = float(input())
fibonacci = [0, 1]
n = len(fibonacci)


while fibonacci[n-1] <= input_number:
    f_new = fibonacci[n-2] + fibonacci[n-1]
    if f_new <= input_number:
        fibonacci.append(f_new)
        n += 1
    else:
        break
print(fibonacci)
