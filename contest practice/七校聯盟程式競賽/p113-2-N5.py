st = input()
ans = [0,0,0,0]
temp = '!@#%^&*'
if len(st) >= 8:
    for i in range(len(st)):
        if st[i].isupper():
            ans[0] += 1
        elif st[i].islower():
            ans[1] += 1
        elif st[i] in temp:
            ans[2] += 1
        elif st[i].isdigit():
            ans[3] += 1
    if ans.count(0) > 0:
        print('0')
    else:
        print('1')
else:
    print('0')