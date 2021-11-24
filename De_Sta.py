def _mean_(li):
    return sum(li) / len(li)
print(_mean_(li))

def _range_(li):
  return [min(li),max(li)]

def _var_(li):
    result = [(row - _mean_(li)) ** 2 for row in li]
    return sum(result) / len(li)

def _std_(li):
  return _var_(li) ** 0.5

def _cv_(li):
  return _std_(li) / _mean_(li)

def _aad_(li):
    result = [abs(row - _mean_(li)) for row in li]
    return sum(result) / len(li)

def _mad_(li):
  result = [abs(row - _median_(li)) for row in li]
  return _median_(result)

def _skewness_(li):
  len_li = len(li)
  result = 0
  for row in li:
    result += ((row - _mean_(li)) / _std_(li)) ** 3
  result = result / len_li
  return result

def _kurtosis_(li):
  result = 0
  li_mean = _mean_(li)
  li_std = _std_(li)
  for row in li:
    result += ((row - li_mean) / li_std) **4
  result = (result / len(li)) -3
  return result

def _median_(li):
  li.sort()
  if len(li) % 2 == 1: return li[int((len(li) - 1) / 2)]
  else: return (li[int(len(li) / 2) - 1] + li[int(len(li) / 2)]) / 2

def _mode_(li):
  li_set = list(set(li))
  li_cnt = [[li.count(row),index] for index, row in enumerate(li_set)]
  li_cnt.sort()
  return li_set[(li_cnt[-1][1])]

def _count_(li):
  li_set = set(li)
  return [li.count(row) for row in li_set]

def iqr(li,p):
  le = len(li)
  sorted_li = sorted(li)
  diff = le * p - int(le*p)
  if diff == 0:
    return sorted_li[int(le * p)-1]
  else:
    return (sorted_li[int(le * p)-1] +  sorted_li[int(le*p)]) / 2

