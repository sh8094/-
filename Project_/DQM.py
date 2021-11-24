import datetime
import time

f = open('Project_/aRaw.csv', 'r', encoding='utf-8-sig')
lines = f.readlines()
dic = {}
data = []
for line in lines:
    line = line.strip().split(',')
    data.append(line)
for key in range(len(data[0])):
    li = []
    for value in range(1,len(data)):
        li.append(data[value][key])
    dic[data[0][key]] = li
f.close()
print(dic)
print('--'*20)
# int, flt: 정수, 실수, None, str 갯수, 인덱스
print('정수')
in_cnt, fl_cnt, no_cnt, st_cnt = 0, 0, 0, 0
in_inx, fl_inx, no_inx, st_inx = [], [], [], []
for i,j in enumerate(dic['im']):
    try:
        int(j)
        in_cnt += 1
        in_inx.append(i)
    except:
        try:
            float(j)
            fl_cnt += 1
            fl_inx.append(i)
        except:
            try:
                if j == None or j== '':
                    no_cnt += 1
                    no_inx.append(i)
                else:
                    st_cnt += 1
                    st_inx.append(i)
            except:
                pass

print(in_cnt, in_inx)
print(fl_cnt, fl_inx)
print(no_cnt, no_inx)
print(st_cnt, st_inx)
print('--'*20)
print('실수')
in_cnt, fl_cnt, no_cnt, st_cnt = 0, 0, 0, 0
in_inx, fl_inx, no_inx, st_inx = [], [], [], []
for i,j in enumerate(dic['fl']):
    try:
        int(j)
        in_cnt += 1
        in_inx.append(i)
    except:
        try:
            float(j)
            fl_cnt += 1
            fl_inx.append(i)
        except:
            try:
                if j == None or j == '':
                    no_cnt += 1
                    no_inx.append(i)
                else:
                    st_cnt += 1
                    st_inx.append(i)
            except:
                pass

print(in_cnt, in_inx)
print(fl_cnt, fl_inx)
print(no_cnt, no_inx)
print(st_cnt, st_inx)
print('--'*20)
# td,dt: dt, td, None, 기타 갯수, 인덱스
print('td')
dt_cnt, td_cnt, no_cnt, el_cnt = 0, 0, 0, 0
dt_inx, td_inx, no_inx, el_inx = [], [], [], []
for i,j in enumerate(dic['td']):
    if '-' in j:
        dt_cnt += 1
        dt_inx.append(i)
    elif 'days' in j:
        td_cnt += 1
        td_inx.append(i)
    elif j == None or j == '':
        no_cnt += 1
        no_inx.append(i)
    else:
        el_cnt += 1
        el_inx.append(i)
print(dt_cnt, dt_inx)
print(td_cnt, td_inx)
print(no_cnt, no_inx)
print(el_cnt, el_inx)
print('--'*20)
print('dt')
dt_cnt, td_cnt, no_cnt, el_cnt = 0, 0, 0, 0
dt_inx, td_inx, no_inx, el_inx = [], [], [], []
for i,j in enumerate(dic['dt']):
    if '-' in j:
        dt_cnt += 1
        dt_inx.append(i)
    elif 'days' in j:
        td_cnt += 1
        td_inx.append(i)
    elif j == None or j == '':
        no_cnt += 1
        no_inx.append(i)
    else:
        el_cnt += 1
        el_inx.append(i)
print(dt_cnt, dt_inx)
print(td_cnt, td_inx)
print(no_cnt, no_inx)
print(el_cnt, el_inx)
print('--'*20)
# oq, no 유일값 갯수
print('oq,no')
print(len(set(dic['oq'])),set(dic['oq']))
print(len(set(dic['no'])),set(dic['no']))
print('--'*20)
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
