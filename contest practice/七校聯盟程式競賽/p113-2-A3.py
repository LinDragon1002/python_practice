st = input()
ans = []
if len(st)-1 == 6:
    for i in range(1,len(st),2):
        ans.append(int(st[i:i+2],16))
    print(f"rgba({ans[0]},{ans[1]},{ans[2]},1.00)")
elif len(st)-1 == 8:
    for i in range(1,len(st)-2,2):
        ans.append(int(st[i:i+2],16))
    ans.append(int(st[-2:],16)/255)
    print(f"rgba({ans[0]},{ans[1]},{ans[2]},{ans[3]:.2f})")
elif len(st)-1 == 3:
    for i in range(1,len(st)):
        ans.append(int(st[i] * 2,16))
    print(f"rgba({ans[0]},{ans[1]},{ans[2]},1.00)")
elif len(st)-1 == 4:
    for i in range(1,len(st)-1):
        ans.append(int(st[i] * 2,16))
    ans.append(int(st[-1]*2,16)/255)
    print(f"rgba({ans[0]},{ans[1]},{ans[2]},{ans[3]:.2f})")