import os
file_Path='D:\YNU_Code\HeadFirstPython\chapter4\sketch.txt'
man_Spoken=[]
other_Spoken=[]
try:
        data=open(file_Path,'r')
        for each_line in data:
                try:
                        (role,spoken)=each_line.split(':',1)
                        spoken=spoken.strip()
                        if role=='Man':
                                man_Spoken.append(spoken)
                        elif role=='Other Man':
                                other_Spoken.append(spoken)
                except ValueError:
                        pass
        data.close()
except IOError:
        print('The file is missing!')
print(man_Spoken)
print(other_Spoken)

#there is a more well method to displaly the following code
"""
try:
        man_Data=open('man_Data.txt','w')
        other_Data=open("other_Data.txt","w")
        print(man_Spoken,file=man_Data)
        print(other_Spoken,file=other_Data)
        man_Data.close() 
        other_Data.close()
except IOError:
        print("Can not write the file correctly!")    
"""

try:
        with open("man_Data.txt",'w') as man_Data:
                print(man_Spoken,file=man_Data)
        with open("other_Data.txt","w") as other_Data: 
                print(other_Spoken,file=other_Data)
except IOError as err:
        print("File error:"+str(err))
#there is no need 'finally' to close the open
