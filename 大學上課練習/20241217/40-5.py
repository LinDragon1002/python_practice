with open ('titanic.csv', 'r')as infile:
    data = infile.readlines()
    data=[d.strip() for d in data]

    C = [0]*2
    Q = [0]*2
    S = [0]*2

    for i in data:
        _,_,result,*_,place = i.split(',')

        if place == 'C':
            if result == '1':
                C[0] += 1
            elif result == '0':
                C[1] += 1
        if place == 'Q':
            if result == '1':
                Q[0] += 1
            elif result == '0':
                Q[1] += 1
        if place == 'S':
            if result == '1':
                S[0] += 1
            elif result == '0':
                S[1] += 1


    print(f'{C[0]/(C[0]+C[1]):.3f},{Q[0]/(Q[0]+Q[1]):.3f},{S[0]/(S[0]+S[1]):.3f}')