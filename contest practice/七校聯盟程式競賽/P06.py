def same():
    st = input()
    ans = 0
    for i in range(len(st)):
        temp = []
        for j in range(i,len(st)):
            temp.append(st[j])
            if len(temp) >= 4 and temp[0] == temp[-1] and temp[0].isupper() and temp[-1].isupper():
                ans += 1
    return ans
print(same())