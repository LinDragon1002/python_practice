st = list(map(int,input().split()))
if st[0] % 2 == 0 and st[1] == st[0] / 2:
    print("YES")
elif st[1] % 2 == 0 and st[0] == st[1] / 2:
    print("YES")
else:
    print("NO")