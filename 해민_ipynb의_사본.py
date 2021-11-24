# -*- coding: utf-8 -*-
"""해민.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WK5mQmCtvXvTfG-Voj1rfgSkzO8z8ySo
"""



import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [20, 10]
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import seaborn as sns
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

## ADF함수
def adf_test(df):
    result = adfuller(df.values)
    print('ADF Statistics : %f' %result[0])
    print('p-value :%f' %result[1])
    print('Critical values:')
    for key , value in result[4].items():
        print('\t%s: %.3f' %(key, value))

def kpss_test(df):
    statistic,p_value,n_lags,critial_values = kpss(df.values)
    print(f'KPSS Statistic : {statistic}')
    print(f'p-value : {p_value}')
    print(f'num lags : {n_lags}')
    print('Critial Values:')
    for key,value in critial_values.items():
        print(f'  {key} : {value}')

start = datetime( 2015, 1, 1 )
end = datetime.now()

# yahoo 파이낸스 
KA = pd.read_csv('data.csv')
KA.head()

def acf(series, k):
    mean = series.mean()
    denominator = np.sum(np.square(series-mean))
    corr = np.sum((series-mean)*(series.shift(k)-mean))
    acf_val = corr/denominator
    return acf_val

acfs=[acf(KA['Close'],k) for k in range(400)]
x = range(400)
fig = plt.figure(figsize=(8,5))
fig.set_facecolor('white')

markers, stemlines, baseline = plt.stem(x, acfs, use_line_collection=True)
markers.set_color('red')
stemlines.set_linestyle('--')
stemlines.set_color('purple')
baseline.set_visible(False)

KA['Close'].plot()
plt.show()

adf_test(KA['Close']) 
# p-value >0.05 귀무가설 채택
## 검정통계량이 critical value 보다 작은 경우 정상성을 띈다고 할 수 있음--> adf 검정통계량이 critical vlaue보다 큼 
### 정상성을 띄지 않음

kpss_test(KA['Close'])
#p-value <0.05 귀무가설 기각
## 검정통계량이 critical value 보다 작은 경우 정상성을 띈다고 할 수 있음--> adf 검정통계량이 critical vlaue보다 큼 
### 정상성을 띄지 않음

# 1차차분 

one_differ_KA = KA['Close'].diff()
one_differ_KA .plot()

one_differ_KA[1:]

#1차 차분값 정상성 확인
adf_test(one_differ_KA[1:])
## p-value <0.05  귀무가설 기각 --> 정상성을 띔

kpss_test(one_differ_KA[1:])
# p-value 귀무가설 채택
# 정상성을 띔

acfs=[acf(one_differ_KA[1:],k) for k in range(400)]
x = range(400)
fig = plt.figure(figsize=(8,5))
fig.set_facecolor('white')

markers, stemlines, baseline = plt.stem(x, acfs, use_line_collection=True)
markers.set_color('red')
stemlines.set_linestyle('--')
stemlines.set_color('purple')
baseline.set_visible(False)

# 1차 차분값을 원데이터에서 빼면 그냥 원데이터인데 한칸씩 밀린 값 만들어짐 

org_differ = KA['Close']-one_differ_KA
org_differ.plot()



#2차 차분
two_differ_KA =  one_differ_KA.diff()
two_differ_KA

adf_test(two_differ_KA[2:])
# 저

KA['Close']