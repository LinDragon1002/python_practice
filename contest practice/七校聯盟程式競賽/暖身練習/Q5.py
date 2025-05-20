num = int(input())
datas = []
for _ in range(num):
    temp = [i for i in input().split(',')]
    datas.append(temp)
datas = sorted(datas,key=lambda x:(int(x[2]),int(x[3])))
main_cnt = 0
for i in range(len(datas)):
    if int(datas[i][3]) == 0:
        main_cnt += 1
        print(f'{main_cnt}.{datas[i][1]}')
        cnt = 0
    else:
        cnt += 1
        print(f'**{main_cnt}-{cnt}.{datas[i][1]}')