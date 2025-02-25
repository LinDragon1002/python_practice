def chess():
    response = input().split(' ')
    number = len(response) // 3
    ans = [[0] * number for _ in range(3)]
    for i in range(3):
        for j in range(number):
            ans[i][j] = int(response[i*number+j])
    for i in range(number):
        temp = []
        for j in range(3):
            temp.append(ans[j][i])
        temp = sorted(temp)
        for j in range(3):
            ans[j][i] = temp[-2]
        
    
    print(ans) 

chess()
    