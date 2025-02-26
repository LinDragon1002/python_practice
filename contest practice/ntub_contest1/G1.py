def chess(a):
    temp = ["將","士","象","車","馬","包","卒"]
    correct = [1,2,2,2,2,2,5]
    ans = [0]*7
    ans1 = []
    for i in range(len(a)):
        for j in range(len(temp)):
            if a[i] == temp[j]:
                ans[j] += 1
    for i in range(len(correct)):
        if correct[i] != ans[i]:
            for j in range(correct[i]-ans[i]):
                ans1.append(temp[i])
    return ans1

a = input()
print(chess(a))