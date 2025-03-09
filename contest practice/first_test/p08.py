def games():
    st = [input(),input(),input()]
    ans = [0,0,0]
    mapping = {"Y":1,"O":2,"X":3}
    st = [mapping[i] for i in st]
    for i in range(2):
        temp = st[i] - st[i+1]
        counts(temp,ans,i,i+1)
        if i == 0:
            temp1 = st[i] - st[i+2]
            counts(temp1,ans,i,i+2)
    if ans.count(0) == 3 or ans.count(1) == 3:
        return 0
    elif ans.count(1) == 2:
        # temp1 = []
        # for i in range(len(ans)):
        #     if ans[i] == 1:
        #         temp1.append(str(i+1))
        # return ",".join(temp1)
        return ",".join([str(i+1) for i in range(len(ans)) if ans[i] == 1])
    else:
        return ans.index(max(ans)) + 1
def counts(temp,ans,i,j):
    if temp == 1 or temp == -2:
        ans[i] += 1
    elif temp == -1 or temp == 2:
        ans[j] += 1
print(games())