def change(scores):
    for i in range(6):
        if scores[i] < 60:
            scores[i] = 60
    return scores

scores1 = [90,80,70,50,40,90]
print(scores1)
scores2 = change(scores1)
print(scores2)
print(scores1)

# 只更改第一個不及格的成績
def change2(scores):
    for i in range(len(scores)):
        if scores[i] < 60:
            scores[i] = 60
            break
    return scores

# 只更改最後一個不及格的成績
def change3(scores):
    for i in range(len(scores)-1, -1, -1):
        if scores[i] < 60:
            scores[i] = 60
            break
    return scores

# 使用 shallow copy
import copy
def change4(scores):
    scores = copy.copy(scores)
    for i in range(len(scores)):
        if scores[i] < 60:
            scores[i] = 60
            break
    return scores

# 刪除list元素
def change5(scores):
    for i in range(len(scores)):
        if scores[i] < 60:
            del scores[i]
            break
    return scores

# 新增list元素
def change6(scores):
    scores.append(max(scores))
    return scores

def change7(scores):
    scores.insert(0, max(scores)+5)
    return scores

# 兩個元素交換
def change8(scores):
    scores[0],scores[1] = scores[1],scores[0]
    return scores

# 旋轉
def change9(scores):
    a = scores.pop(0)
    scores.append(a)
    return scores

# 反轉
def change10(scores):
    scores.reverse()
    return scores

# 複製
def change11(scores):
    scores1 = scores*2
    scores2 = [s for s in scores for _ in range(2)]
    return scores1, scores2

# 交換
def change12(scores):
    st = [i for i in input()]
    st[0],st[1] = st[1],st[0]
    return "".join(st)

# 判斷字串內容都不同
def change13(scores):
    s = {i for i in scores}
    return len(s) == len(scores)

# 排列
def change14(scores):
    from itertools import permutations
    return list(permutations(scores))

# 組合

