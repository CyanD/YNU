import os
import time
import sys
import yate
import cgi
import cgitb
cgitb.enable()

addr=os.environ['REMOTE_ADDR']
host=os.environ['REMOTE_HOST']
method=os.environ['REQUEST_METHOD']

cur_time=time.asctime(time.localtime())
print(yate.start_response("text/html"))
print("HOST:"+host+"<br/>"+" Address:"+addr+"<br/> Time:"+cur_time+"<br/> Method:"+method)

form=cgi.FieldStorage()
for each_form_item in form.keys():
    print(each_form_item+"->"+form[each_form_item].value,end='',file=sys.stderr)
print(file=sys.stderr)
print("<br/>OK.")
