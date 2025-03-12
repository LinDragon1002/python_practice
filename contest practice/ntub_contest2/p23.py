def voc():
    st = [i for i in input().split(" ")]
    number = 1
    temp = []
    while number <= len(st):
        for i in range(len(st)):
            if int(st[i][-1]) == number:
                temp.append("".join(["" if i.isdigit() else i for i in st[i]]))
        number += 1
    return " ".join(temp)
print(voc())