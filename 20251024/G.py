tot_ans = []
for i in range(int(input())):
    ans = -60000
    temp = input().split(' ')
    for j in range(1,int(temp[0])):
        for k in range(j+1,int(temp[0])+1):
            ans = max(ans,int(temp[j]) - int(temp[k]))
    tot_ans.append(ans)
for i in tot_ans:
    print(i)