def counts():
    num1,num2 = int(input()),int(input())
    ans = []
    for i in range(num1,num2+1):

        temp = [v for v in str(i)]
        if temp.count("0") == 0:
            temp1 = 0
            for j in range(len(temp)):
                if i % int(temp[j]) == 0:
                    temp1 += 1
                else:
                    break
                if temp1 == len(temp):
                    ans.append(i)
    return ans
print(counts())