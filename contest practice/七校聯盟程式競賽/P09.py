def counts():
    st = [i.strip() for i in input().split(",")]
    ans = []
    for i in range(len(st)):
        number = int(st[i],3)
        bin_str = bin(number)[2:]
        ans.append(bin_str)
    return ans
print(counts())