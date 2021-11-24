import datetime
import time

ts = [0,1,2,3]

def ts_to_dt(ts):
    dt = [datetime.datetime.fromtimestamp(i) for i in ts]
    return dt
print(ts_to_dt(ts))

dt = ts_to_dt(ts)
def dt_to_ts(dt):
    ts = [time.mktime(i.timetuple()) for i in dt]
    return ts
print(dt_to_ts(dt))

def dt_to_str(dt):
    str = [i.strftime('%Y-%m-%d %H-%M-%S') for i in dt]
    return str
print(dt_to_str(dt))

str=dt_to_str(dt)
def str_to_dt(st):
    dt = [datetime.datetime.strptime(i, '%Y-%m-%d %H-%M-%S') for i in st]
    return dt
print(str_to_dt(str))

# datetime을 - 연산시켜서 timedelta로 변환 그 다음 - 시켜준 값을 + 해줌
#  1970.01.01.00.00.00을 빼고 다시  1970.01.01.00.00.00을 더하여 timedelta로 변환
def dt_to_td(dt):
    t_0 = datetime.datetime.fromtimestamp(0)
    t_1 = datetime.timedelta(719559,32400) #719559d, 32400s는 1970.01.01.09.00.00임
    dt_new = dt - t_0
    result = dt_new + t_1
    return result

# timedelta to datetime으로 변환
def td_to_dt(td):
    t_0 = datetime.datetime.fromtimestamp(0)
    t_1 = datetime.timedelta(719559,32400)
    result = td - t_1
    result = t_0 + result
    return result
t = datetime.timedelta(10000)
print(td_to_dt(t))
# td_1 = datetime.timedelta(719559,324000) 1970.01.01.09.00.00

# timedelta를 timestamp로 변환
# timedelta의 일수를 초로 변환시키고 1970.01.01.09.00.00 초를 빼서 timestamp를 만듬
# 1970.01.01.00.00.00 미만의 timedelta는 변환이 안됨
def td_to_ts(td):
    ts = (td.days * 86400) + td.seconds
    return ts

# timestamp를 timedelta로 변환

def ts_to_td(ts):
    return datetime.timedelta(seconds=ts)
ts = td_to_ts(datetime.timedelta(1,1))

def td_to_str(td):
    return str(td)

st='1 day, 0:00:01'

def str_to_td(st):
    a = st.replace(' day, ', ':')
    a = a.split(':')
    d = int(a[0])
    s = int(a[1]) * 3600
    s += int(a[2]) * 60
    s += int(a[3])
    return datetime.timedelta(d,s)
print(str_to_td(st))
print(datetime.timedelta(days=1,weeks=10))


