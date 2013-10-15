def toList(Name="julie.txt"):
        temp=[];
        try:
                with open(Name) as julie_Time:
                        for each_Time in julie_Time.readline().split(","):
                                each_Time=each_Time.strip()
                                temp.append(each_Time)
        except IOError as err:
                print("IOError:"+str(err))
        print(temp)

toList("julie.txt")
toList("james.txt")
toList("mikey.txt")
toList("sarah.txt")
