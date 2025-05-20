from itertools import permutations
num = input()
op = len(num)
cnt = 0
while True:
    if int(num) == 0 or int(num) == 495 or int(num) == 6174:
        break
    temp = []
    if len(num) < op:
        num = "0" * (op-len(num)) + num
    for i in permutations(num):
        temp.append("".join(i))
    temp = sorted(temp)
    num = str(abs(int(temp[0]) - int(temp[-1])))
    if int(temp[0] )!= int(temp[-1]):
        cnt += 1
print(cnt)