import sqlite3

connection=sqlite3.connect('coachdata.sqlite')
cursor=connection.cursor()#import!!!
cursor.execute("""create table athlete(
id integer primary key autoincrement unique not null,
name text not null,
dob date not null)""")
cursor.execute("""create table timing_data(
athlete_id integer not null,
value text not null,
foreign key(athlete_id) references athletes)""")
connection.commit()
connection.close()
