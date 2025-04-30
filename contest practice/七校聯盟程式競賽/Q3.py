st = input().split("=")
cnt = 0
while True:
    if eval(st[0],{"Y":cnt}) == int(st[1]):
        print(cnt)
        break
    cnt += 1
