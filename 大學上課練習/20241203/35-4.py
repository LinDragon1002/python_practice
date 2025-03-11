with open('lotto.csv','r') as infile, open('out.csv','w') as outfile:
    data = infile.readlines()
    data = [d.strip() for d in data]

    temp = []
    hit = ('32','15','7','20','33','5')
    # tot = [0]*7
    tot = {str(i):0 for i in range(1,39)}

    for i in data:
        count = 0
        no,n1,n2,n3,n4,n5,n6 = i.split(',')
        number = [n1,n2,n3,n4,n5,n6]

        for d in range(len(number)):
            tot[number[d]] += 1
            if number[d] in hit:
                number[d] += '*'
                count += 1
            else:
                number[d] += ' '

        # tot[count] += 1

        # temp.append(f'{no:>4}  {number[0]:>3} {number[1]:>3} {number[2]:>3} {number[3]:>3} {number[4]:>3} {number[5]:>3}\n')
        temp.append(f'{no:>4}  {"  ".join(f"{n:>3}" for n in number)}  {count:>3}\n')


    temp[-1] = temp[-1].strip()
    outfile.writelines(temp)

    for key in tot:
        rate = tot[key] / len(data)
        if rate > 0.17:
            print(f'號碼{key}有{tot[key]}筆投注,比率為{rate:.3f}')

    # for i in range(len(tot)):
    #     print(i,tot[i])