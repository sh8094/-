import datetime
import time
from DATA_Q import Quality
import pandas

new_dict = {}
contents = []
with open('aRaw.csv' , 'r',encoding='utf-8-sig') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip().split(',')
        contents.append(line)
    for key in range(len(contents[0])):
        new_dict[contents[0][key]] = [contents[value][key] for value in range(1, len(contents))]

quality_dict = Quality.final_qulity(new_dict)
# print(new_dict)
# print(quality_dict)
class Analysist:
    def __init__(self,new_dict):
        self.new_dict = new_dict

    def DT_to_int(li):
        li = [time.mktime(date_t.timetuple()) for date_t in li ]
        return li
    def TD_to_int(li):
        li = [time_d.total_seconds()for time_d in li ]
        return li
    def mean(li):
        return sum(li)/len(li)

    def median(li):
        li.sort()
        if len(li) % 2 == 1:
            return li[int((len(li) - 1) / 2)]
        else:
            return (li[int(len(li) / 2) - 1] + li[int(len(li) / 2)]) / 2

    def diff(li):

        diff_list=[x-Analysist.mean(li) for x in li]
        return diff_list

    def STD(li):

        diff_2_list  = [x**2 for x in Analysist.diff(li)]

        std = (sum(diff_2_list)/len(diff_2_list))**(1/2)
        return std

    def IQR(li):
        li = pandas.Series(li)
        Q1 = li.quantile(.25)
        Q3 = li.quantile(.75)

        return Q3-Q1

    def AAD(li):

        AA = [abs(x - Analysist.mean(li)) for x in li]

        return Analysist.mean(AA)

    def MAD(li):
        result = [abs(x - Analysist.median(li)) for x in li ]
        return Analysist.median(result)

    def skewness(li):
        result = [((row - Analysist.mean(li)) / Analysist.STD(li)) ** 3 for row in li]
        s = sum(result) / len(result)

        return s
    def kurtosis(li):
        result = [((x - Analysist.mean(li)) / Analysist.STD(li)) ** 4 for x in li]
        result = (sum(result) / len(li)) - 3
        return result
#
    def all_stat(self):
        new_dict = self
        for key, val in new_dict.items():

            if all(isinstance(x, str) for x in [x for x in val['value'] if x is not None]):
                pass
            elif all(isinstance(x, datetime.datetime) for x in [x for x in val['value']]):
                turn_li = Analysist.DT_to_int(val['value'])
                print('---------------', key, '---------------')
                print('IQR    :  ',  Analysist.IQR(val['value']))
                print('STD    :  ',  Analysist.STD(turn_li))
                print('AAD    :  ',  Analysist.AAD(turn_li))
                print('MAD    :  ',  Analysist.MAD(turn_li))
                print('Skewness  :  ', Analysist.skewness(turn_li))
                print('Kurtosis  :  ',  Analysist.kurtosis(turn_li))
                print('----------------------------------------')
            elif all(isinstance(x, datetime.timedelta) for x in [x for x in val['value']]):
                turn_li = Analysist.TD_to_int(val['value'])
                print('---------------', key, '---------------')
                print('IQR    :  ', Analysist.IQR(val['value']))
                print('STD    :  ',  Analysist.STD(turn_li))

                print('AAD    :  ', Analysist.AAD(turn_li))
                print('MAD    :  ', Analysist.MAD(turn_li))
                print('Skewness  :  ', Analysist.skewness(turn_li))
                print('Kurtosis  :  ', Analysist.kurtosis(turn_li))
                print('----------------------------------------')
            else:
                turn_li  = val['value']
                print('---------------',key,'---------------')
                print('STD    :  ', Analysist.STD(turn_li))
                print('IQR    :  ',  Analysist.IQR(turn_li))
                print('AAD    :  ', Analysist.AAD(turn_li))
                print('MAD    :  ', Analysist.MAD(turn_li))
                print('Skewness  :  ', Analysist.skewness(turn_li))
                print('Kurtosis  :  ',Analysist.kurtosis(turn_li))
                print('----------------------------------------')

Analysist.all_stat(quality_dict)

class Divide:
    num = 10
    def __init__(self,quality_dict):
        self.quality_dict = quality_dict

    def DI_len(li):
        max_li = max(li)
        min_li = min(li)
        rem = max_li-min_li
        di_len = rem/Divide.num
        remain = di_len - int(di_len)
        if remain <0.5:
            di_len = round(di_len)+1
        else:
            di_len = round(di_len)
        return di_len

    def section(li):
        di_len = Divide.DI_len(li)
        minimum = min(li)
        section_li = [minimum]
        for x in range(Divide.num):
            minimum  = minimum +di_len
            section_li.append(minimum)
        return section_li

    def Distrib(li):
        dist = {}
        for index, value in enumerate(Divide.section(li)):
            count = 0
            dist[value] = {'index': [], 'value': [], 'count': []}
            for i,val in enumerate(li):
                if val>=value and val<Divide.section(li)[index+1]:
                    dist[value]['index'].append(i)
                    dist[value]['value'].append(val)
                    count+=1
            dist[value]['count'].append(count)
        return dist

    def col(self):
        new_dict = self
        A = {}
        for key, val in new_dict.items():
            if all(isinstance(x, str) for x in [x for x in val['value'] if x is not None]):
                pass
            elif all(isinstance(x, datetime.datetime) for x in [x for x in val['value']]):
                turn_li = Analysist.DT_to_int(val['value'])
                DT = Divide.Distrib(turn_li)
                for k , v in DT.items():
                    v['value'] = [datetime.datetime.fromtimestamp(x) for x in v['value']]
                    KK = datetime.datetime.fromtimestamp(k)

                    DT[KK]  = DT.pop(k)
                A[key] = DT
            elif all(isinstance(x, datetime.timedelta) for x in [x for x in val['value']]):
                turn_li = Analysist.TD_to_int(val['value'])
                TD = Divide.Distrib(turn_li)
                for k , v in TD.items():
                    v['value'] = [pandas.to_timedelta(str(datetime.timedelta(seconds=x))) for x in v['value']]
                    KK = pandas.to_timedelta(str(datetime.timedelta(seconds=k)))

                    TD[KK] = TD.pop(k)
                A[key] = TD
            else:
                A[key] =  Divide.Distrib(val['value'])
        return A


# STD , iqr, AAD, MAD, 왜도 첨도
# 구간으로 나누기
