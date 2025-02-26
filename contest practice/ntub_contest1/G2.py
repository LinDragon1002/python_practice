def chess(a):
    temp = ["將","帥","士","仕","象","相","車","俥","馬","傌","包","炮","卒","兵"]
    correct = [1,1,2,2,2,2,2,2,2,2,2,2,5,5]
    correct1 = [7,7,6,6,5,5,4,4,3,3,2,2,1,1]
    count = {char: a.count(char) for char in temp}
    ans = [temp[i] for i in range(14) for _ in range(correct[i] - count.get(temp[i], 0))]
    ans1 = 0
    for i in range(len(ans)):
        for j in range(len(temp)):
            if temp[j] == ans[i]:
                ans1 += correct1[j]
         
    return ans1

a = input()
print(chess(a))