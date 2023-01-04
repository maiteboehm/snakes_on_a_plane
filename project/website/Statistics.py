from CharReader import Dictionary_Creater
import os
Path = os.path.abspath(os.curdir)
print(Path)
Project_Path = os.path.dirname(Path)
print(Project_Path)
ChartIn_Path = Path + r'\Input_Data\\'
print(ChartIn_Path)
Resorted_Dictionary = Dictionary_Creater(ChartIn_Path)
print(Resorted_Dictionary)
