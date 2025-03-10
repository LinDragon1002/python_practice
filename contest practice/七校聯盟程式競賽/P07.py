def counts():
    st = list(input())
    ans = []
    def counting(number):
        ans = 0
        while number[0] > 0 and number[1] < len(st)-1 and st[number[0]-1] == st[number[1]+1]:
            number[0] -= 1
            number[1] += 1
            temp.append(st[number[0]])
            temp.append(st[number[1]])
        temp1 = list(set(temp))
        if len(temp1) >= 3:
            ans = max(ans,len(temp))
        return ans
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            number = [i,i+1]
            temp = [st[i],st[i+1]]
            ans.append(counting(number))
        elif st[i-1] == st[i+1]:
            number = [i-1,i+1]
            temp = [st[i-1],st[i],st[i+1]]
            ans.append(counting(number))
    return max(ans)
print(counts())