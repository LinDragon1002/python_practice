def total(a):
    temp = ['E','D','C','B','A']
    ans = 0
    for i in range(len(a)):
        for j in range(5):
            if a[i] == temp[j]:
                ans += j + 1
    return ans

a = input()
print(total(a))