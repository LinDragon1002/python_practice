n = 7
temp = format(n,"b")
ans = 3
for i in temp:
    if ans == 3:
        ans = i
    elif ans == i:
        print(False)
    ans = i
else:
    print(True)

# 另解
'''
x = bin(n)[2:]
return "11" not in x and "00" not in x
'''