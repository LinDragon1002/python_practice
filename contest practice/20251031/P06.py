st1 = input()
st2 = input()
temp_list1 = []
temp_list2 = []
ans = 0
for i in range(len(st1)):
    for j in range(i+1,len(st1)):
        temp_list1.append(st1[i:j])
for i in range(len(st2)):
    for j in range(i+1,len(st2)):
        temp_list2.append(st2[i:j])
ans_list = list(set(temp_list1) & set(temp_list2))
for i in ans_list:
    ans = max(len(i),ans)
print(ans)