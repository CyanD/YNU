def sanitize(time_String):
        if "-" in time_String:
                splitter='-'
        elif ':' in time_String:
                splitter=':'
        else:
                return(time_String)
        (mins,secs)=time_String.split(splitter)
        return(mins+"."+secs)

class Athlet:
        def ___init__(self,a_Name,a_Dob=None,a_Times=[]):
                self.Name=a_Name
                self.Dob=a_Dob
                self.Times=a_Times

        def top3(self):
                return(sorted([sanitize(each) for each in self.Times])[0:3])
        def add_Time(self,time):
                self.Times.append(time)
        def add_Times(self,times):
                self.Times.extend(times)

                
def get_Coach_Data(file_Name):
        try:
                with open(file_Name) as f:
                        data=f.readline()
                        temp1=data.strip().split(",")
                        #the following code can be simplified, but why it can not work!!!????
                        result=Athlet()
                        result.Name=temp1.pop(0)
                        result.Dob=temp1.pop(0)
                        result.Times=temp1
                        return(result)
                        #return(Athlet(temp1.pop(0),temp1.pop(0),temp1))
        except IOError as ioerr:
                print("File Error:"+ioerr)
                return(None)

ath=get_Coach_Data("julie2.txt")
print(ath.Name+"'s fastest times are:"+str(ath.top3()))


ath=get_Coach_Data("james2.txt")
ath.add_Time('0.11')
print(ath.Name+"'s fastest times are:"+str(ath.top3()))
