import datetime

import pandas
import pandas as pd
new_dict = {}
contents = []
with open('aRaw.csv' , 'r',encoding='utf-8-sig') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip().split(',')
        contents.append(line)
    for key in range(len(contents[0])):
        new_dict[contents[0][key]] = [contents[value][key] for value in range(1, len(contents))]

class find_dup:
    def __init__(self,new_dict):
        self.new_dict = new_dict
    def find_dup_col(self):
        dup_col = {'key':[],'value':[]}
        set_col = []
        for key,val in self.items():
            if val in set_col:
                dup_col['key'].append(key)
                dup_col['value'].append(val)
            else:
                set_col.append(val)
        return dup_col

    def find_dup_row(self):
        dup_row = []
        set_row = []
        dict_list = [list(x) for x in zip(*self.values())]
        dict_list.insert(0, list(self.keys()))
        for index, val in enumerate(dict_list):
            if val in set_row:
                dup_row.append(index)
            else:
                set_row.append(val)
        return dup_row
# 중복행
def find_dup_row(new_dict):
    dup_row =[]
    set_row=[]
    dict_list = [list(x) for x in zip(*new_dict.values())]
    dict_list.insert(0, list(new_dict.keys()))
    for index, val in enumerate(dict_list):
        if val in set_row:
            dup_row.append(index)
        else:
            set_row.append(val)
    return dup_row

class Type:
    def __init__(self,li):
        self.li = li
        self.num_index, self.none_index, self.float_index, self.str_index, self.dt_index, self.td_index = [], [], [], [], [], []
        self.num_value, self.none_value, self.float_value, self.str_value, self.dt_value, self.td_value = [], [], [], [], [], []
        self.all_dict={}
    def confirm(self):
        for index, value in enumerate(self.li):
            try:
                int(value)
                self.num_index.append(index)
                self.num_value.append(int(value))
            except TypeError:
                self.none_index.append(index)
                self.none_value.append(value)
            except ValueError:
                try:
                    float(value)
                    self.float_index.append(index)
                    self.float_value.append(float(value))
                except ValueError:
                    if value == '':
                        self.none_index.append(index)
                        self.none_value.append(value)
                    else:
                        try:
                            pd.to_timedelta(value)
                            self.td_index.append(index)
                            self.td_value.append(pd.to_timedelta(value))
                        except ValueError:
                            try:
                                datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                                self.dt_index.append(index)
                                self.dt_value.append(datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S'))
                            except ValueError:
                                self.str_index.append(index)
                                self.str_value.append(value)

        self.all_dict['int']={'index':self.num_index, 'value':self.num_value}
        self.all_dict['float']={'index':self.float_index, 'value':self.float_value}
        self.all_dict['None']={'index':self.none_index, 'value':self.none_value}
        self.all_dict['str']={'index':self.str_index, 'value':self.str_value}
        self.all_dict['dt']={'index':self.dt_index, 'value':self.dt_value}
        self.all_dict['td']={'index':self.td_index, 'value':self.td_value}
        return self.all_dict
    def int(self):
        self.confirm()
        return self.all_dict['int']
    def float(self):
        self.confirm()
        return self.all_dict['float']
    def none(self):
        self.confirm()

        return self.all_dict['None']
    def str(self):
        self.confirm()
        return self.all_dict['str']
    def str_count(self):
        self.confirm()
        str = {}
        for s in set(self.str_value):
            s_count = self.str_value.count(s)
            str[s] = s_count
        return str
    def dt(self):
        self.confirm()
        return self.all_dict['dt']

    def td(self):
        self.confirm()
        return self.all_dict['td']
    def count(self):
        self.confirm()
        count_dict={'key':[],'count':[]}
        for key,val in self.all_dict.items():
            count_dict['key'].append(key)
            count_dict['count'].append(len(val['value']))
        max_index = count_dict['count'].index(max(count_dict['count']))

        return (count_dict['key'][max_index],self.all_dict[count_dict['key'][max_index]]['index'])
    def turn(self):
        count = self.count()
        for key in count:
            if key == 'dt':
                return self.dt()
            elif key == 'td':
                return self.td()
            elif key == 'int':
                return self.int()
            elif key == 'float':
                return self.float()
            elif key == 'str':
                return self.str()
            else:
                return self.none()
import time
import pandas as pd

class outlier:
    def __init__(self,li_dict):
        self.li_dict = li_dict

    def IQR_OUTLIER(self):

        if all(isinstance(x,datetime.datetime) for x in self['value']):
            li= [time.mktime(date_t.timetuple()) for date_t in self['value']]
        elif all(isinstance(x,datetime.timedelta) for x in self['value']):
            li = [x.total_seconds() for x in self['value']]
        else:
            li = self['value']
        li = [x for x in li if x is not None]
        li = pandas.Series(li)
        Q1 = li.quantile(.25)
        Q3 = li.quantile(.75)
        IQR = Q3 - Q1
        minimum = Q1 - 1.5 * IQR
        maximum = Q3 + 1.5 * IQR

        outlier_dict = {'index': [], 'value': []}
        for index, value in enumerate(li):

            if minimum >= value or maximum <= value:
                outlier_dict['index'].append(self['index'][index])
                outlier_dict['value'].append(self['value'][index])
        return outlier_dict

    def median(li):
        li.sort()
        if len(li) % 2 == 1:
            return li[int((len(li) - 1) / 2)]
        else:
            return (li[int(len(li) / 2) - 1] + li[int(len(li) / 2)]) / 2

    def MAD_OUTLIER(self):
        if all(isinstance(x, datetime.datetime) for x in [x for x in self['value'] if x is not None]):
            cur_li = [time.mktime(date_t.timetuple()) for date_t in self['value'] if date_t is not None]
        elif all(isinstance(x, datetime.timedelta) for x in [x for x in self['value'] if x is not None]):
            cur_li = [x.total_seconds() for x in self['value'] if x is not None]
        else:
            cur_li = [x for x in self['value'] if x is not None]

        meadian = outlier.MEADIAN(cur_li)

        diff_list = [abs(x - meadian) for x in cur_li]

        MAD = outlier.MEADIAN(diff_list)
        Mi_list = [(0.6745 * x) / MAD for x in diff_list]
        cut_off = 3.5
        mad_outlier = {'index': [], 'value': []}

        for index, value in enumerate(Mi_list):
            if value >= cut_off:
                try:
                    mad_outlier['index'].append(self['index'][self['value'].index(cur_li[index])])
                    mad_outlier['value'].append(self['value'][self['value'].index(cur_li[index])])
                except ValueError:
                    try:
                        i = cur_li[index]
                        A = str(datetime.timedelta(seconds=i))
                        A = pd.to_timedelta(A)
                        mad_outlier['index'].append(self['index'][self['value'].index(A)])
                        mad_outlier['value'].append(self['value'][self['value'].index(A)])
                    except ValueError:
                        i = cur_li[index]
                        A = datetime.datetime.fromtimestamp(i)

                        mad_outlier['index'].append(self['index'][self['value'].index(A)])
                        mad_outlier['value'].append(self['value'][self['value'].index(A)])

        return mad_outlier

    def Z_SCOER(self):
        if all(isinstance(x,datetime.datetime) for x in[x for x in self['value'] if x is not None]):
            cur_li = [time.mktime(date_t.timetuple()) for date_t in self['value'] if date_t is not None]
        elif all(isinstance(x,datetime.timedelta) for x in [x for x in self['value'] if x is not None]):
            li = self['value']
            cur_li = [x.total_seconds()for x in self['value'] if x is not None ]

        else:
            cur_li = [x for x in self['value'] if x is not None]

        li_mean = sum(cur_li)/len(cur_li)

        diff_list =[(x-li_mean)**2 for x in cur_li]
        s = (sum(diff_list)/len(diff_list))**(1/2)
        z_score = [ (y-li_mean)/s for y in cur_li]

        z_outlier = {'index':[],'value':[]}

        for index, value in enumerate(z_score):
            if abs(value)>=3:
                try :
                    z_outlier['index'].append(self['index'][self['value'].index(cur_li[index])])
                    z_outlier['value'].append(self['value'][self['value'].index(cur_li[index])])
                except ValueError:
                    try:
                        i = cur_li[index]
                        A=str(datetime.timedelta(seconds=i))
                        A = pd.to_timedelta(A)

                        z_outlier['index'].append(self['index'][self['value'].index(A)])
                        z_outlier['value'].append(self['value'][self['value'].index(A)])
                    except ValueError:
                        i = cur_li[index]
                        A = datetime.datetime.fromtimestamp(i)

                        z_outlier['index'].append(self['index'][self['value'].index(A)])
                        z_outlier['value'].append(self['value'][self['value'].index(A)])
        return z_outlier

print(outlier.Z_SCOER(new_dict))
        # 추가
# 중복 삭제(가장 앞에 index 살려두기), data type 안 맞는 것 none , outlier none, missing value percentile , interpolration 평균( 명목형 최빈값중 가장 앞선 index 살려두기)
# 데이터 읽어와서 데이터 타입의 인덱스를 체크하고 그 빈도수를 확인하여 가장 알맞은 자료형 픽스 (이후 이건 none처리 전에 해야 함)

# STD , iqr, AAD, MAD, 왜도 첨도
# 구간으로 나누기
