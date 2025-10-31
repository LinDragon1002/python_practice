n = int(input())
ans = []
for i in range(n):
    temp_list = []
    for j in range(int(input())):
        temp = input()
        temp_list.append(str(temp.find("#")+1))
    ans.append(temp_list)
for i in ans:
    temp = i[::-1]
    print(" ".join(temp))