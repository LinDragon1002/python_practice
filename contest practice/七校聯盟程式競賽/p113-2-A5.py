num1 = int(input())
std = [[0,"","",0,0,0] for _ in range(num1)]

for i in range(num1):
    temp = input().split()
    for j in range(3):
        std[i][j] = temp[j]
num2 = int(input())

for i in range(num2):
    temp = input().split()
    for j in range(len(std)):
        if int(temp[0]) == int(std[j][0]):
            std[j][3] += int(temp[-1])
            std[j][4] += 1

for i in range(len(std)):
    if std[i][4] != 0:
        std[i][5] = std[i][3] / std[i][4]
    else:
        std[i][5] = 0

std = sorted(std,key= lambda x:(-x[-1],int(x[0]))) #要注意學生id是數字，但是我存在list裡面是字串

for i in range(len(std)):
    print(f'{std[i][0]} {std[i][1]} {std[i][2]} {std[i][-1]:.2f}')
