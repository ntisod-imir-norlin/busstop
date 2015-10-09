from datetime import datetime

dt = datetime.strptime('2015-10-09T12:52:50','%Y-%m-%dT%H:%M:%S')

dt2 =datetime.now()

timediff=dt2-dt

print timediff

print "{hour}:{minute:02d}".format(hour=dt.hour,minute=dt.minute)