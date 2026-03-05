num1 = "456"
num2 = "77"
maxnum = max(len(num1),len(num2))

temp = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
num1 = num1.zfill(maxnum)
num2 = num2.zfill(maxnum)
ans = ""
tempadd = 0

for i in range(maxnum-1,-1,-1):
    tempnum = temp[num1[i]] + temp[num2[i]] + tempadd
    if tempnum > 9:
        tempadd = int(str(tempnum)[0])
    else:
        tempadd = 0
    ans += str(tempnum)[-1]

if tempadd > 0:
    ans += str(tempadd)

print(ans[::-1])


import sys
sys.set_int_max_str_digits(10000) 
x = int(num1)
y = int(num2)

# return str(x+y)
print()