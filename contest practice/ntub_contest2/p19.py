def useword():
    ar = [sorted(i) for i in input().split(" ")]
    ans = []
    for i in range(len(ar[0])):
        number = 0
        for j in range(1,len(ar)):
            if ar[0][i] in ar[j]:
                ar[j].remove(ar[0][i])
                number += 1
        if number == len(ar)-1:
            ans.append(ar[0][i])
    return "".join(sorted(ans))
print(useword())
