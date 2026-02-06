num = 0
if len(str(num)) == 1:
    print(num)
else:
    temp = num
    while len(str(temp)) > 1:
        temp_num = 0
        for i in str(temp):
            temp_num += int(i)
        temp = temp_num
    print(temp)