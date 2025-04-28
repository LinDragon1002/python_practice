num1 = int(input())
num2 = int(input())

cnt = 0

while True:
    num2 = num2 / num1
    cnt += 1
    if num1 > num2:
        print(cnt)
        break