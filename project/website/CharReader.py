import os
import string

Path = os.path.abspath(os.curdir)
ChartIn_Path = Path +'\Input_Data\\'

def Dictionary_Resorter(Dictionary):

    Resorted_Dictionary = {

    }
    for key in Dictionary:
        Temp_Liste = []
        #print(Filename_Dictionary[key])
        for index,Row_List in enumerate(Dictionary[key]):
            Temp_Liste2 = []
            if index>9:
                Number = str(''.join(Row_List[0:2]))
                print(Number)
            else:
                Number = str(Row_List[0])
                #print(Number)

            for ind,Seat in enumerate(Row_List):

                if Seat.isdigit():
                    continue
                else:
                    #print(Number,ind,Seat)
                    Seat_ID = ''.join([Number,Seat])
                    Temp_Liste2.append(str(Seat_ID))
            Temp_Liste.append(Temp_Liste2)
        Resorted_Dictionary.update({key:Temp_Liste})

    return(Resorted_Dictionary)

def Dictionary_Creater(Filepath):
    Filename_Liste = []
    Filename_Dictionary = {

    }
    Flight_Number = 1
    for Filename in os.listdir(Filepath):
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
        Filename_Dictionary.update({Flight_Number:Filename_Input})
        print(Flight_Number)
        Flight_Number+=1
        Resorted_Dictionary = Dictionary_Resorter(Filename_Dictionary)
    return(Resorted_Dictionary)





