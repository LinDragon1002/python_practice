num = int(input())
cnt = 2
temp = "1"
while True:
    if num == 1:
        print(f"1>=1")
        break
    else:
        temp += "+" + str(cnt)
        if eval(temp) >= num:
            print(f"{temp}>={num}")
            break
        cnt += 1
