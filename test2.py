import datetime
import time

dic = {}
data = []
with open('KW.csv' , 'r',encoding='utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(',')
        data.append(line)
    for key in range(len(data[0])):
        dic[data[0][key]] = [data[value][key] for value in range(1, len(data))]
# print(dic)
# print('--'*20)

# 중복행렬 im, fl, td, dt
print('중복행')
dic_itm = list(dic.items())
dic_val = list(dic.values())
b = []
c = []
a = list(zip(*dic_val))
for i, val in enumerate(a):
    if val in b:
        c.append([i,val])
    else:
        b.append(val)
b=[]
for i in range(len(c)):
    b.append(c[i][0])
print(b)
print(c)
print('--'*20)
print('중복열')
dic_itm = list(dic.items())
dic_val = list(dic.values())
b = []
c = []
for key,val in dic_itm:
    if val not in b:
        b.append(val)
    else:
        c.append([key,val])
b=[]
for i in range(len(c)):
    b.append(c[i][0])
print(b)
print(c)
print('--'*20)
print(dic['SDT'][0])
def str_to_dt(st):
    dt = [datetime.datetime.strptime(i,'%Y-%m-%d %H:%M:%S') for i in st]
    return dt
# print(str_to_dt(dic['SDT']))
dt = str_to_dt(dic['SDT'])
def dt_to_ts(dt):
    ts = [time.mktime(i.timetuple()) for i in dt]
    return ts
print(dt_to_ts(dt))
