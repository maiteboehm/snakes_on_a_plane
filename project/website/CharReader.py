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
    'Filename':[['0','A','B','C'],['1','A','X','C'],['2','A','B','C']],
    'Filename1':[['0','A','B','C'],['1','A','B','C'],['2','A','B','C']]
}
def Dictionary_Resorter(Dictionary):

    Resorted_Dictionary = {

    }
    for key in Dictionary:
        Temp_Liste = []
        #print(Filename_Dictionary[key])
        for index,Row_List in enumerate(Dictionary[key]):
            Temp_Liste2 = []
            for ind,Seat in enumerate(Row_List):
                if ind == 0:
                    Temp_Liste2.append(Row_List[0])
                else:
                    Seat_ID = ''.join([Row_List[0],Seat])
                    Temp_Liste2.append(Seat_ID)
            Temp_Liste.append(Temp_Liste2)
        Resorted_Dictionary.update({key:Temp_Liste})
    return(Resorted_Dictionary)
print(Dictionary_Resorter(Test_Dictionary))


