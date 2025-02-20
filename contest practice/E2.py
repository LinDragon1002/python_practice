def rome2list(a):
    temp = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    list = []
    ans = 0
    for i in range(len(a)):
        if a[i] in temp:
            list.append(temp[a[i]])
    for i in range(len(list)):
        if i < len(list)-1 and list[i] < list[i+1]:
            ans -= list[i]
        else:
            ans += list[i]

    return ans
a = input()
print(rome2list(a))