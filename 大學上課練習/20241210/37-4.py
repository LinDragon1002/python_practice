with open ('cake.csv','r') as infile, open ('out.csv','w',encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]

    temp = []
    total = 0

    for i in data:
        no, *quantity = i.split(',')

        quantity = [int(q) for q in quantity]

        cnt = 0
        for d in quantity:
            if d == 2:
                cnt+=1
        if cnt >= 3:
            print(f'編號:{no}')
            total += 1
    print(total)