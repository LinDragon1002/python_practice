def exchange():
    st = [i for i in input().split(" ")]
    ans = []
    for i in range(len(st)):
        temp = [i for i in st[i]]
        temp1 = ""
        for j in range(len(temp)-1,-1,-1):
            temp1 += temp[j]
        ans.append(temp1)
    return " ".join(ans)
print(exchange())