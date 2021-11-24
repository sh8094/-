#평균
def _mean_(li):
    x = sum(li) / len(li)
    return x
#자유도
def _df_(li):
    n = len(li) - 1
    return n
#표본표준편차
def _std_(li):
    s = [(i - _mean_(li)) ** 2 for i in li]
    s = (sum(s) / _df_(li)) ** 0.5
    return s
# 단일표본 T-test
def t_test(li,m):
    t = (_mean_(li)-m)/(_std_(li)/len(li)**0.5)
    return t

li = [495,496,502,494,499,501,493]
m = 500
print('단일표본')
print('평균:',_mean_(li))
print('자유도:',_df_(li))
print('표준편차:',_std_(li))
print('t-통계량:',t_test(li,m))
print('--'*20)
# 독립표본 T-test
def t_test2(li_a,li_b):
    n_a = _df_(li_a);    n_b = _df_(li_b)
    m_li_a = _mean_(li_a);    m_li_b = _mean_(li_b)
    s_a = sum((i - m_li_a)**2 for i in li_a);    s_b = sum((i - m_li_b)**2 for i in li_b)
    t = (s_a + s_b)/(n_a + n_b)
    return t

li_a = [44,44,56,46,47,38,58,53,49,35,46,30,41]
li_b = [35,47,55,29,40,39,32,41,42,57,51,39]
print('독립표본')
print('t-통계량:',t_test2(li_a,li_b))
print('--'*20)

# 카이제곱검정
def x2_test(li_a,li_b):
    x = []
    x2 = 0
    [x.append(j - li_b[i]) for i,j in enumerate(li_a)]
    for i,j in enumerate(li_b):
            x2 += x[i]**2/j
    return x2
ob = [25,15,15,45]
ep = [16,24,24,36]
print('카이제곱검정')
print('X2-통계량:',x2_test(ob,ep))
print('--'*20)

#F-검정
def f_test(li_a,li_b):
    s2_a = _std_(li_a)**2;s2_b = _std_(li_b)**2
    f = s2_a/s2_b
    return f
li_a = [272,255,278,282,296,312,356,296,302,312]
li_b = [276,280,369,285,303,317,290,250,313,307]
print('F-검정')
print('f-통계량:',f_test(li_a,li_b))

