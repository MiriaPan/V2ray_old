import sha2
import time
import datetime

def now_times():
	now_time = time.strftime('%Y-%m-%d')
	shaz = sha2.sha256(now_time + 'lucy').hexdigest()
	return shaz

def wl_times():
	timelb = []
	for z in range(1,8):
		nowtime=datetime.datetime.now()
		detaday=datetime.timedelta(days=z)
		da_days=nowtime+detaday
		wltime = da_days.strftime('%Y-%m-%d')
		timelb.append(wltime)
		now_time = time.strftime('%Y-%m-%d')
		timelb.append(now_time)
	return timelb

def put_time():
	timexx = wl_times()
	with open('/Users/lucy/Desktop/V2rayx/V2ray/core/time.txt','w') as x:
		x.write(str(timexx))

def times():
	now_tim = time.strftime('%Y-%m-%d')
	return now_tim
