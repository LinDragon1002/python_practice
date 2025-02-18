with open('lotto.csv','r') as infile, open('out.csv','w',encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [d.strip() for d in data]

    temp = []
    hit = ('32','15','7','20','33','5')



    for i in data:
        count = 0
        no,n1,n2,n3,n4,n5,n6 = i.split(',')
        number = [n1,n2,n3,n4,n5,n6]

        for d in range(len(number)):
            if number[d] in hit:
                number[d] += '*'
                count += 1
            else:
                number[d] += ' '

        if count == 3:
            tot = 300
        elif count == 4:
            tot = 1000
        elif count == 5:
            tot = 35000
        elif count == 6:
            tot = 1000000
        else:
            tot = 0

        # temp.append(f'{no:>4}  {number[0]:>3} {number[1]:>3} {number[2]:>3} {number[3]:>3} {number[4]:>3} {number[5]:>3}\n')
        temp.append(f'{no:>4}  {"  ".join(f"{n:>4}" for n in number)}  ({tot:,.0f}元)\n')


    temp[-1] = temp[-1].strip()
    outfile.writelines(temp)