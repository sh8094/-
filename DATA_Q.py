import datetime
import pandas as pd
import time
from DATA_E import find_dup
from DATA_E import Type
from DATA_E import outlier

new_dict = {}
contents = []
with open('aRaw.csv' , 'r',encoding='utf-8-sig') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(',')
        contents.append(line)
    for key in range(len(contents[0])):
        new_dict[contents[0][key]] = [contents[value][key] for value in range(1, len(contents))]

class Quality:
    def __init__(self,new_dict):
        self.new_dict = new_dict
    def del_dup(self):
        dup_row = find_dup.find_dup_row(self)
        dup_col = find_dup.find_dup_col(self)

        for key in dup_col['key']:
            del self[key]

        for index in dup_row[::-1]:
            for key, value in self.items():
                del value[index-1]
        return self

    def clear_type(self):
        new_dict = self
        clear_dict = {}
        for key, col in new_dict.items():
            right_index = Type(col).turn()
            iindex = right_index['index']
            for x in range(len(col)):
                if x not in iindex:
                    col[x] = None
                else:
                    tr_i = iindex.index(x)
                    col[x] = right_index['value'][tr_i]
            clear_dict[key] = {'index': [x for x in range(len(col))], 'value': [x for x in col]}
        return clear_dict

    def clear_outlier(self, method='zscore'):
        new_dict = self
        clear_dict = {}
        for key, val in new_dict.items():

            try:
                if method == 'IQR':
                    outlier_dict = outlier.IQR_OUTLIER(val)

                elif method == 'mad':
                    outlier_dict = outlier.MAD_OUTLIER(val)
                else:

                    outlier_dict = outlier.Z_SCOER(val)

                for v in outlier_dict['index']:
                    val['value'][v] = None
                clear_dict[key] = val
            except TypeError:
                val = val
                clear_dict[key] = val
        return clear_dict

    def mean_dict(li):
        if all(isinstance(x, datetime.datetime) for x in [x for x in li if x is not None]):
            cur_li = [time.mktime(date_t.timetuple()) for date_t in li if date_t is not None]
            li_mean = sum(cur_li) / len(cur_li)
            return datetime.datetime.fromtimestamp(li_mean)
        elif all(isinstance(x, datetime.timedelta) for x in [x for x in li if x is not None]):
            cur_li = [x.total_seconds() for x in li if x is not None]
            li_mean = sum(cur_li) / len(cur_li)
            li_mean = str(datetime.timedelta(seconds=li_mean))
            li_mean = pd.to_timedelta(li_mean)
            return li_mean
        elif all(isinstance(x, int) for x in [x for x in li if x is not None]):
            cur_li = [x for x in li if x is not None]
            li_mean = sum(cur_li) / len(cur_li)
            return round(li_mean)
        else:
            cur_li = [x for x in li if x is not None]
            li_mean = sum(cur_li) / len(cur_li)
            return li_mean

    def fill(self):
        new_dict = self
        fill_dict = {}
        for key, val in new_dict.items():
            if all(isinstance(x, str) for x in [x for x in val['value'] if x is not None]):
                count = 0
                mode = 0
                for key, value in Type(val['value']).str_count().items():
                    if value > count:
                        mode = key

                for i, v in enumerate(val['value']):
                    if v is None:
                        val['value'][i] = mode

            else:
                li_mean = Quality.mean_dict(val['value'])
                for i, v in enumerate(val['value']):
                    if v is None:
                        val['value'][i] = li_mean
            fill_dict[key] = val
        return fill_dict

    def final_qulity(self):
        clear_dup = Quality.del_dup(self)

        clear_type_dict = Quality.clear_type(clear_dup)
        clear_outlier_dict = Quality.clear_outlier(clear_type_dict,'mad')
        fill_dict = Quality.fill(clear_outlier_dict)

        return fill_dict

