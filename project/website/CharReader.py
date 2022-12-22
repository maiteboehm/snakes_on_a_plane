import os
import string

Filename_Liste = []
#print(os.getcwd())
Path = os.path.abspath(os.curdir)
Project_Path = os.path.dirname(Path)
#print('Path', Project_Path)
ChartIn_Path = Project_Path +'\Input_Data\\'
#print(os.listdir())
Filename_Dictionary = {

}

for Filename in os.listdir(ChartIn_Path):
    Filename_Input = []

    if Filename.endswith('.txt'):
        Filename_Liste.append(Filename)
        Input = open(ChartIn_Path+str(Filename),mode = 'r')

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

Test_Dictionary = {
    'Filename':[['0','A','B','C'],['1','A','B','C'],['2','A','B','C']],
    'Filename1':[['0','A','B','C'],['1','A','B','C'],['2','A','B','C']]
}
for key in Test_Dictionary:
    #print(Filename_Dictionary[key])
    for i in Test_Dictionary[key]:
        print(i)
        for Seat in i:
            print(Seat)
            if str(Seat) == 'X':
                print('True',key)

