st = input()
temp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
if len(st) % 3 == 0:
    for i in range(0,len(st),3):
        if st[i:i+2] == '00':
            ans += " " * int(st[i+2])
        else:
            ans += temp[int(st[i:i+2]) - 1] * int(st[i+2])
    print(ans)
else:
    print("Error")