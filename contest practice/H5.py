def number():
    response = int(input())
    ans = []
    for i in range(2,response+1):
        if response%i == 0:
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                ans.append(i)
    print(ans)

number()