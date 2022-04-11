from datetime import datetime
import time


def timeStamp_to_dateTime(timeStamp):
    return datetime.fromtimestamp(int(timeStamp)/1000).strftime('%Y-%m-%d %H:%M:%S')


def dateTime_to_timeStamp(dt_string):
    return int(time.mktime(datetime.strptime(dt_string, '%Y-%m-%d').timetuple())*1000)


    #  '%Y-%m-%d %H:%M:%S'




now = datetime.now()
#dt_string = now.strftime("%Y-%m-%d %H:%M")

ts = now.timestamp()


#print(ts)


timestamp = 1645437058.948
#1643295600
dt_obj = datetime.fromtimestamp(timestamp)

print('date time: ', dt_obj)

