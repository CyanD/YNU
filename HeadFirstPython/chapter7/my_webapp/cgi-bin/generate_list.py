import athletemodel
import yate
import glob

import cgitb
cgitb.enable()

data_files=glob.glob("./data/*.txt")
athletes=athletemodel.put_to_store(data_files)
print(yate.start_response())
print(yate.include_header("Coach Kelly's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.para("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    print(yate.radio_button("which_athlete",athletes[each_athlete].Name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home":"../index.html"}))

##print("""<html>
##<head>
##<title>Coach Kelly's List of Athletes</title>
##<link type="text/css" rel="stylesheet" href="../coach.css" />
##</head>
##<body>
##<h1>Coach Kelly's List of Athletes</h1>
##
##<form action="generate_timing_data.py" method="POST">
##<p>Select an athlete from the list to work with:</p>
##<input type="radio" name="which_athlete" value="Julie Jones">Julie Jones<br />
##<input type="radio" name="which_athlete" value="Sarah Sweeney">Sarah Sweeney<br />
##<input type="radio" name="which_athlete" value="Mikey McManus">Mikey McManus<br />
##<input type="radio" name="which_athlete" value="James Lee">James Lee<br />
##<p></p><input type=submit value="Select">
##<p>
##<a href="../index.html">Home</a>&nbsp;&nbsp;&nbsp;&nbsp;
##</p>
##</body>
##</html>""")
