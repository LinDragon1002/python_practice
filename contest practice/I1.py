from math import sqrt
def chess():
    response = input().split(' ')
    number = int(sqrt(len(response)))
    temp = [["0"] * number for _ in range(number)]
    for i in range(number):
        for j in range(number):
            temp[i][j] = response[i*number+j]

    for i in range(number):
        for j in range(number,0,-1):
            if temp[j-1][i] == temp[i][j-1]:
                ans = True
            else:
                ans = False
                break
    print(ans) 

chess()
    