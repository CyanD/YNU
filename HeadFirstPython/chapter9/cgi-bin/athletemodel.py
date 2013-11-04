def sanitize(time_String):
        if "-" in time_String:
                splitter='-'
        elif ':' in time_String:
                splitter=':'
        else:
                return(time_String)
        (mins,secs)=time_String.split(splitter)
        return(mins+"."+secs)

class AthleteList(list):
    def __init__(self,a_Name,a_Dob=None,a_Times=[]):
        list.__init__([])
        self.Name=a_Name
        self.Dob=a_Dob
        self.extend(a_Times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

"""vera=AthleteList("vera vi")
vera.append("4.3")
print(vera.top3())
vera.extend(["3.4","3.2","1.2"])
print(vera.top3())
print(vera.Name)
print(vera.Dob)
print(vera)"""


def get_Coach_Data(file_Name):
        try:
                with open(file_Name) as f:
                        data=f.readline()
                        temp1=data.strip().split(",")
                        #the following code can be simplified, but why it can not work!!!????
                        """result=Athlet()
                        result.Name=temp1.pop(0)
                        result.Dob=temp1.pop(0)
                        result.Times=temp1
                        return(result)"""
                        #return(Athlet(temp1.pop(0),temp1.pop(0),temp1))
                        return(AthleteList(temp1.pop(0),temp1.pop(0),temp1))
        except IOError as ioerr:
                print("File Error:"+ioerr)
                return(None)

import pickle
def put_to_store(files_list):
    all_athletes={}
    for each_file in files_list:
        ath=get_Coach_Data(each_file)
        all_athletes[ath.Name]=ath
    try:
        with open("athletes.pickle",'wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as ioerr:
        print("File Error(put_and_store):"+str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes={}
    try:
        with open("athletes.pickle",'rb') as athf:
            all_athletes=pickle.load(athf)
    except IOError as ioerr:
        print("File Error(get_from_store):"+str(ioerr))
    return(all_athletes)
