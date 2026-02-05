n = 5
temp_list = [n]
while len(str(n ** 2)) > 1:
    temp = 0
    for i in str(n):
        temp += int(i) ** 2
    if temp in temp_list:
        break
    temp_list.append(temp)
    n = temp


if n == 1:
    print(True)
else:
    print(False)