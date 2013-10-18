def sanitize(time_String):
        if "-" in time_String:
                splitter='-'
        elif ':' in time_String:
                splitter=':'
        else:
                return(time_String)
        (mins,secs)=time_String.split(splitter)
        return(mins+"."+secs)

def get_Coach_Data(file_Name):
        try:
                with open(file_Name) as f:
                        data=f.readline()
                return(data.strip().split(","))
        except IOError as ioerr:
                print("File Error:"+ioerr)
                return(None)


#print([sanitize(each) for each in get_Coach_Data('sarah2.txt')[2:14]])
sarah=get_Coach_Data('sarah2.txt')
'''(name,dob)=sarah.pop(0),sarah.pop(0)
print(name+"'s fastest times are:"+
      str(sorted([sanitize(each) for each in sarah])[0:3]))
'''

#use dictionary to show the result, funciton is as same as above
sarah_Dict=dict()
sarah_Dict['Name']=sarah.pop(0)
sarah_Dict['Dob']=sarah.pop(0)
sarah_Dict['Time']=sarah
print(sarah_Dict["Name"]+"'s fastest times are:"+
      str(sorted([sanitize(each) for each in sarah_Dict['Time']])[0:3]))
