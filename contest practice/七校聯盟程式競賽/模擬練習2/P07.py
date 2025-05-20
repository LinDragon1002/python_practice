st = input().split("=")
temp = ["+","-","*","/"]
cnt = 0
for i in range(len(temp)):
    temp1 = st[0].replace("Y",f"{temp[i]}")
    for j in range(1,101):
        if int(st[1]) == eval(temp1,{"X":j}):
            cnt += 1
            break
print(cnt)