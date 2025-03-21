from itertools import permutations
def permutation(st):
    ans = []
    for i in permutations(st):
        temp = ''.join(i)
        for j in range(len(i)-1):
            if i[j] == i[j+1]:
                break
        else:
            ans.append(temp)
    return len(set(ans))
print(permutation('adaded'))
print(permutation('114354'))
