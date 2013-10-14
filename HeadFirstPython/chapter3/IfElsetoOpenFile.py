"""Method: if-else judgement, need to think about all the posibility.
Function: open file sketch, and add 'said' after role in every line,
and judge whether exists error."""
import os
file_Path='D:\YNU_Code\HeadFirstPython\chapter3\sketch.txt'
if os.path.exists(file_Path):
        data=open(file_Path,'r')
        for each_line in data:
                if each_line.find(':')>=0:
                        (role,spoken)=each_line.split(':',1)
                        print(role+' said:'+spoken,end='')
        data.close()
else:
        print("The file is not existed!")


