"""Method: try-catch way, do not need to think about all the posibility.
Function: open file sketch, and add 'said' after role in every line,
and judge whether exists error."""
import os
file_Path='D:\YNU_Code\HeadFirstPython\chapter3\sketch.txt'
try:
        data=open(file_Path,'r')
        for each_line in data:
                try:
                        (role,spoken)=each_line.split(':',1)
                        print(role+' said:'+spoken,end='')

                except ValueError:
                        pass
        data.close()
except IOError:
        print("The file is not existed!")
        
