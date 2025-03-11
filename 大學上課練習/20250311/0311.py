def compae_score(**kwargs):
    total = 0
    for key in kwargs:
        total += kwargs[key]
    avg = total / len(kwargs)
    return avg

# print(compae_score(A1=90, A5=80, C1=70))

'''
順序:
(1)positional
(2)keyword
'''
def compate_sore(chi,eng,**kwargs):
    if chi < 60 or eng < 60:
        return False
    if len(kwargs) < 3:
        return False
    '''
    cnt = 0
    for key in kwargs:
        if kwargs[key] <= 60:
            cnt += 1
    if cnt >= 1:
        return False
    '''
    # 值的轉換 A1=60, A2=50, A3=40 -> [0,1,1]
    cnt = sum([1 if kwargs[key]<60 else 0 for key in kwargs])
    # 值的過濾 A1=60, A2=50, A3=40 -> [1,1]
    cnt = sum([1 for key in kwargs if kwargs[key]<60])
    return cnt<1
print(compate_sore(90, 80, A1=60, A2=50, A3=40))
print(compate_sore(90, 80, A1=70, A2=80, A3=90))