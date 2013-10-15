def toList(Name="julie.txt"):
        temp=[];
        try:
                with open(Name) as julie_Time:
                        for each_Time in julie_Time.readline().split(","):
                                each_Time=each_Time.strip()
                                temp.append(each_Time)
        except IOError as err:
                print("IOError:"+str(err))
        return(temp)

def sanitize(time_String):
        if ":" in time_String:
                splitter=":"
        elif "-" in time_String:
                splitter="-"
        else:
                return(time_String)
        (mins,secs)=time_String.split(splitter)
        return(mins+'.'+secs)

def print_f(List):
        list_Pro=[]
        for each in List:
                each_New=sanitize(each)
                list_Pro.append(each_New)
        print(list_Pro)
                

print(toList("julie.txt"))
print(toList("james.txt"))
print(toList("mikey.txt"))
print(toList("sarah.txt"))

print_f(toList("julie.txt"))
print_f(toList("james.txt"))
print_f(toList("mikey.txt"))
print_f(toList("sarah.txt"))

print([sanitize(each) for each in toList("julie.txt")])

james=sorted([sanitize(each) for each in toList("james.txt")])
unique_james=[]
for each in james:
        if each not in unique_james:
                unique_james.append(each)
print(unique_james)
print(unique_james[0:3])


#set: another test
a=set()#set is one of factory function
a={34,343,3435,24,34,34}#to produce a set
print(len(a))
b=['few','fewaa','aa','aa']
A=set(b)# convert a list to a set
print(A)
