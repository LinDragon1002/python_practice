num = int(input())
cnt = 0
while num != 0:
    temp = []
    for i in str(num):
        temp.append(int(i))
    temp = sorted(temp,reverse=True)
    num -= temp[0]
    cnt += 1
print(cnt)