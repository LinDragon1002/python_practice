st = [int(i) for i in input().split(',')]
st = list(sorted(st))
for i in range(len(st)):
    for j in range(len(st)):
        if st[j] % st[i] != 0:
            print(0)
            break
    else:
        print(1)
    break