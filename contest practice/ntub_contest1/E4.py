def MyStr(a):
    ans = {}
    ans1 = {}
    for i in set(a):
        if i not in ans:
            ans[i] = a.find(i)
        if i not in ans1:
            ans1[i] = a.rfind(i)
    ans = dict(sorted(ans.items(), key= lambda i:i[1]))
    ans1 = dict(sorted(ans1.items(), key= lambda i:i[1]))
    '''
    ans2 = ""
    for i in ans:
        ans2 += i
    print(ans2)
    '''
    print("".join(ans.keys()))
    '''
    ans3 = ""
    for i in ans1:
        ans3 += i
    print(ans3)
    '''
    print("".join(ans1.keys()))

a = input()
MyStr(a)