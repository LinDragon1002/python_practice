word = "GooG"
temp = [0,0]

for i in range(len(word)):
    if word[i].isupper():
        if word.index(word[i]) == 0 or temp[0] == i:
            temp[0] += 1
        else:
            print(False)
            break
    else:
        temp[1] += 1

if temp[0] == 0 or temp[1] == 0 or word[0].isupper() and temp[0] == 1:
    print(True)
else:
    print(False)