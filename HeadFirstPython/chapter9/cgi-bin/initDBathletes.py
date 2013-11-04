import sqlite3
connection=sqlite3.connect("coachdata.sqlite")
cursor=connection.cursor()

import glob
import athletemodel
data_files=glob.glob("../data/*.txt")
athletes=athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name=athletes[each_ath].Name
    dob=athletes[each_ath].Dob

    cursor.execute("insert into athlete (name,dob) values(?,?)",(name,dob))
    connection.commit()
connection.close()
