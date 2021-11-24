# raw[‘im’] = [‘’, None, 1, 1.0, 1.1, ‘1 days 00:00:01’, ‘2000-01-01 00:00:01’, ‘All’, ‘SF’]
# 1-1) 판다스를 이용해 딕셔너리를 csv 파일로 저장
# 1-2) 판다스를 이용해 1-1)을 불러와 딕셔너리로 저장
import pandas as pd
raw={}
raw['im'] = ['',None, 1, 1.0, 1.1, '1 days 00:00:01', '2000-01-01 00:00:01', 'All', 'SF']
df=pd.DataFrame(raw)
df.to_csv('ct2.csv')
print(df)

df2=df.to_dict('list') # 승훈
print(df2)

data = pd.read_csv('ct2.csv')  #주환
dic_pd_1 = {}
dic_pd_1[data.columns[1]] = data['im'].values.tolist()
print(dic_pd_1)

new_dict={}  #해민
contents=[]
with open('ct2.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        contents.append(line)
    new_dict[contents[0]]=contents[1:]
f.close()
print(new_dict)

# 2-1) open을 이용해 딕셔너리를 csv 파일로 저장
# 2-2) open을 이용해 2-1)을 불러와 딕셔너리로 저장
# 3) 1-2)와 2-2) 딕셔너리 값 비교할 수 있게 출력
# 준수 : csv 파일 열 이름 : im, 딕셔너리 키 : im

raw={}
raw['im'] = ['',None, 1, 1.0, 1.1, '1 days 00:00:01', '2000-01-01 00:00:01', 'All', 'SF']

key_list=['im'] # 해민
with open('ct2_2.csv', 'w') as f:
    for key in key_list:
        f.write('%s' % key)
        f.write('\n')
        for x in range(len(raw['im'])):
            f.write('%s' % raw['im'][x])
            f.write('\n')

f = open("../open.csv", "w", encoding='utf8') #주환
f.write('im' + '\n')
for x in raw['im']:
    x = str(x)
    f.write(x + '\n')


# new_dict={}  #해민
# contents=[]
# with open('ct2_2.csv', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.strip()
#         contents.append(line)
#     new_dict[contents[0]]=contents[1:]
# f.close()
# print(lines)
# print(contents)
# print(new_dict)

f = open("../open.csv", 'r', encoding='utf8')  #주환
dic_open_1 = {}
lines = f.readlines()
for index in range(len(lines)):
    lines[index] = lines[index].strip()
dic_open_1[lines[0]] = lines[1:]
f.close()
print(lines)
print(line)
print('dic_open_1: ',dic_open_1)

raw = {} #주환
raw['num'] = ['1', '1.0', '1.1', '', None, 'All', 'SF']
raw['td'] = ['1', '1.0', '1.1', '', None, '1 days 00:00:00', 'All']
raw['dt'] = ['1', '1.0', '1.1', '', None, '2000-01-01 00:00:00', 'All']
raw['cat'] = ['', None, 'All', '12+', 'All', '18+']
cnt_int, cnt_flt0, cnt_flt, cnt_no, cnt_str = 0, 0, 0, 0, 0
idx_int, idx_flt0, idx_flt, idx_no, idx_str = [],[],[],[],[]
for i, v in enumerate(raw['num']):
    try:
        int(v)
        cnt_int += 1
        idx_int.append(i)
    except:
        try:
            if float(v)-int(float(v)) == 0:
                cnt_flt0 += 1
                idx_flt0.append(i)
            elif  float(v)-int(float(v)) != 0:
                cnt_flt += 1
                idx_flt.append(i)
        except:
            if v == '' or v == None:
                cnt_no += 1
                idx_no.append(i)
            else:
                cnt_str += 1
                idx_str.append(i)


print("정수: {}, 개수: {}".format(idx_int, cnt_int))
print("실수0: {}, 개수: {}".format(idx_flt0, cnt_flt0))
print("실수: {}, 개수: {}".format(idx_flt, cnt_flt))
print("None: {}, 개수: {}".format(idx_no, cnt_no))
print("str: {}, 개수: {}".format(idx_str, cnt_str))


#승훈
raw = {}
raw['num'] = ['1', '1.0', '1.1', '', None, 'All', 'SF']
raw['td'] = ['1', '1.0', '1.1', '', None, '1 days 00:00:00', 'All']
raw['dt'] = ['1', '1.0', '1.1', '', None, '2000-01-01 00:00:00', 'All']
raw['cat'] = ['', None, 'All', '12+', 'All', '18+']
cnt_int, cnt_flt0, cnt_flt, cnt_no, cnt_str = 0, 0, 0, 0, 0
idx_int, idx_flt0, idx_flt, idx_no, idx_str = [],[],[],[],[]
for i, v in enumerate(raw['num']):
    try:
        int(v)
        cnt_int += 1
        idx_int.append(i)
    except:
        try:
            if float(v)-int(float(v)) == 0:
                cnt_flt0 += 1
                idx_flt0.append(i)
            elif  float(v)-int(float(v)) != 0:
                cnt_flt += 1
                idx_flt.append(i)
        except:
            if v == '' or v == None:
                cnt_no += 1
                idx_no.append(i)
            else:
                cnt_str += 1
                idx_str.append(i)


print("정수: {}, 개수: {}".format(idx_int, cnt_int))
print("실수0: {}, 개수: {}".format(idx_flt0, cnt_flt0))
print("실수: {}, 개수: {}".format(idx_flt, cnt_flt))
print("None: {}, 개수: {}".format(idx_no, cnt_no))
print("str: {}, 개수: {}".format(idx_str, cnt_str))


#해민
print('딕셔너리 raw의 키 num의 값을 읽고 다음 개수, 인덱스 구하기')
print('정수 문자열, 소수점 이하가 0인 실수 문자열, 소수점 이하가 0이 아닌 실수 문자열, None('')포함')

int_index, flt0_index, flt1_index, none_index, str_index = [],[],[],[],[]
int_cnt, flt_cnt0, flt_cnt1, none_cnt, str_cnt = 0,0,0,0,0
for index, row in enumerate(raw['num']):
    if None == row:
        none_cnt += 1
        none_index.append(index)
    else:
        try:
            row = int(row)
            int_cnt += 1
            int_index.append(index)
        except ValueError:
            try:
                row = float(row)
                row_int = int(row)
                if row - row_int == 0:
                    flt_cnt0 += 1
                    flt0_index.append(index)
                else:
                    flt_cnt1 += 1
                    flt1_index.append(index)
            except ValueError:
                if '' == row:
                    none_cnt += 1
                    none_index.append(index)
                else:
                    str_cnt += 1
                    str_index.append(index)

count = {'int': int_cnt ,'float.0': flt_cnt0, 'float not 0':flt_cnt1, 'None':none_cnt, 'Str':str_cnt}
print(count)
index = {'int': int_index ,'float.0': flt0_index, 'float not 0':flt1_index, 'None':none_index, 'Str':str_index}
print(index)

print('딕셔너리 raw의 키 td의 값을 읽고 다음 개수, 인덱스 구하기')
td_cnt, none_cnt, etc_cnt = 0,0,0
td_index, none_index, etc_index = [],[],[]
print('timedelta 문자열, None("포함)')
for index,row in enumerate(raw['td']):
    if None == row or '' == row:
        none_cnt += 1
        none_index.append(index)
    elif 'days' in row:
        td_cnt += 1
        td_index.append(index)
    else:
        etc_cnt += 1
        etc_index.append(index)
count = {'td':td_cnt,'None':none_cnt,'etc': etc_cnt}
index = {'td':td_index,'None':none_index,'etc':etc_index}
print(count)
print(index)

print('3딕셔너리 raw의 키 dt의 값을 읽고 다음 개수, 인덱스 구하기')
print('datetime 문자열, None(''포함)')
etc_cnt, dt_cnt, none_cnt = 0,0,0
etc_index, dt_index, none_index = [],[],[]

for index, row in enumerate(raw['dt']):
    if None == row or '' == row:
        none_cnt += 1
        none_index.append(index)
    elif ':' in row:
        try:
            row = datetime.datetime.strptime(row, '%Y-%m-%d %H:%M:%S')
            dt_cnt += 1
            dt_index.append(index)
        except:
            pass
    else:
        etc_cnt += 1
        etc_index.append(index)
count = {'dt': dt_cnt, 'None': none_cnt, 'etc': etc_cnt}
index = {'dt': dt_index, 'None' : none_index, 'etc' : etc_cnt}
print(count)
print(index)

print('딕셔너리 raw의 키 cat의 값을 읽고 각 값의 개수, 인덱스 구하기')
none_cnt, str_cnt = 0,0
none_index, str_index = [],[]
for index, row in enumerate(raw['cat']):
    if '' == row or None == row:
        none_cnt += 1
        none_index.append(index)
    else:
        str_cnt += 1
        str_index.append(index)
count = {'str':str_cnt,'None':none_cnt}
index = {'str':str_index,'None':none_index}
print(count)
print(index)
