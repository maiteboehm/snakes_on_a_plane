# assignment 1
# Task 02 - Reversed Words

# start of code
import numpy as np

print("Please, input word")
input_word = input()
word_array1 = np.array(list(input_word))
counter = 1
word_array2 = []

for n in word_array1:
    #print(word_array1[len(word_array1)-counter])
    word_array2.append(word_array1[len(word_array1)-counter])
    counter = counter + 1

output_word = "".join(word_array2)
print(output_word)
