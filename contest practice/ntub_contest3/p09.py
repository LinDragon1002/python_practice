num = int(input())
a = 1
b = 1
ans = "1,1"
if num == 1:
    print("1")
else:
    for i in range(2,num):
        if i % 2 == 0:
            a = a + b
            ans += f",{a}"
        else:
            b = a + b
            ans += f",{b}"

    print(ans)