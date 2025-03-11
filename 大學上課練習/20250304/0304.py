# (1) 傳int(immutable物件，不可變物件)給函式
def myfunction(arg):
    print('函式1', arg, hex(id(arg)))
    arg+=1
    print('函式2',arg, hex(id(arg)))
    return
value = 100
print('主程式1',value, hex(id(value)))
myfunction(value)
print('主程式2',value, hex(id(value)))


# (2) 傳list(mutable物件，可變物件)給函式
def myfunction1(arg):
    print('函式1', arg, hex(id(arg)))
    arg[0]+=1
    print('函式2',arg, hex(id(arg)))
    return
value = [1,2,3,4,5]
print('主程式1',value, hex(id(value)))
myfunction1(value)
print('主程式2',value, hex(id(value)))


import copy
# (3) shallow copy(淺拷貝)
def myfunction2(arg):
    arg = copy.copy(arg)
    print('函式1', arg, hex(id(arg)))
    # arg[0] = 'A'
    arg[4][0] = 'A' # 修改第二層會影響原本的list
    print('函式2',arg, hex(id(arg)))
    return
# value = [1,2,3,4,5]
value2 = [1,2,3,4,[5,6,7]]
print('主程式1',value2, hex(id(value2)))
myfunction2(value2)
print('主程式2',value2, hex(id(value2)))


# (4) deep copy(深拷貝)
def myfunction3(arg):
    arg = copy.deepcopy(arg)
    print('函式1', arg, hex(id(arg)))
    arg[4][0] = 'A'
    print('函式2',arg, hex(id(arg)))
    return
value = [1,2,3,4,[5,6,7]]
print('主程式1',value, hex(id(value)))
myfunction3(value)
print('主程式2',value, hex(id(value)))


#  2 傳入多個str
def ispass(*rank):
    cnt = 0
    for r in rank:
        if r == "A":
            cnt+=1
    if cnt >= 1:
        return True
    return False
print(ispass("A","B","C"))
print(ispass("B","C","D"))

def ispass2(*rank):
    cnt = rank.count("A")
    if cnt >= 1:
        return True
    return False
print(ispass2("A","B","C"))
print(ispass2("B","C","D"))

def ispass3(*rank):
    return rank.count("A")>=1
print(ispass3("A","B","C"))
print(ispass3("B","C","D"))

# 3 傳入多個int
def ispass4(*scores):
    if len(scores) == 0:
        return False
    avg = sum(scores)/len(scores)
    return avg >= 60
print(ispass4(50,60,70))
print(ispass4(50,40,30))

def ispass5(*scores):
    scores = sorted(list(scores))
    if len(scores) // 2 == 1:
        return scores[len(scores)//2] >= 60
    return scores[len(scores)//2-1] >= 60
print(ispass5(50,60,70))
print(ispass5(50,30,40,80))

def ispass6(*scores):
    scores_set = set(scores)
    scores_dict = {}
    for i in scores_set:
        scores_dict[i] = scores.count(i)
    return max(scores_dict.values())
print(ispass6(50,50,60,60,60,60,70,70,70))

