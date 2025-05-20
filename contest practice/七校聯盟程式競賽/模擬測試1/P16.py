num = int(input())
ans = []
ans.append(num)
while num != 1:
    if num % 2 == 0 and num >=4:
        num //= 4
    elif num % 2 == 0 and num <4:
        num //= 2
    else:
        num = num * 5 + 1
    ans.append(num)
print(*ans,sep='->')