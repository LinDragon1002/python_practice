num = int(input())
temp = ['0','1']
if num != 1:
    for i in range(1,num):
        ans = []
        for j in range(num**2):
            if num ** 2 // 2 > j:
                ans.append('0' + temp[j % 2])
            else:
                ans.append('1' + temp[j % 2])
        temp = ans.copy()
for i in temp:
    print(i)