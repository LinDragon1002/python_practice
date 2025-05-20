num = input().split()
if int(num[0]) % 2 == 0 and int(num[1]) == int(num[0]) // 2:
    print("YES")
elif int(num[1]) % 2 == 0 and int(num[0]) == int(num[1]) // 2:
    print("YES")
else:
    print('NO')