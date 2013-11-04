import cgi
import yate
import cgitb
cgitb.enable()
print(yate.start_response("text/html"))
print(yate.do_form("add_timing_data.py",["TimeValue"],text="Send"))
