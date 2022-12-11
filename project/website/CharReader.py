import os
import string

Filename_Liste = []
#print(os.getcwd())
#print(os.listdir())
Filename_Dictionary = {

}

for Filename in os.listdir(r'C:\Users\max_b\Desktop\Python for DataScientist\Input_Data_ASR_Project'):
    Filename_Input = []

    if Filename.endswith('.txt'):
        Filename_Liste.append(Filename)
        Input = open(r'C:\Users\max_b\Desktop\Python for DataScientist\Input_Data_ASR_Project\\'+str(Filename),mode = 'r')

        for index,line in enumerate(Input):
            line.lstrip()
            Line_Liste = []

            for letter in line:

                if letter !='\t' and letter !='\n':
                    Line_Liste.append(letter)

            if Line_Liste[0]=='A':
                Line_Liste.insert(0, '0')
            if Line_Liste[0]=='1' and index == 0:
                Letter_Liste = list(string.ascii_uppercase)
                Tmp_Liste = [str(index)]

                for i in range(len(Line_Liste)-1):
                    Tmp_Liste.append(Letter_Liste[i])

                Filename_Input.append(Tmp_Liste)

            Filename_Input.append(Line_Liste)
    Filename_Dictionary.update({Filename:Filename_Input})
print(Filename_Dictionary)
