with open ('card.csv','r', encoding='utf-8') as infile, open ('out.csv','w', encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]
    
    temp = []
    std = 'BCDADABCDBAABCADCBDC'
    
    for d in data:
        no, ans = d.split(',')
        
        tot = 0
        check = [None]*20
        for i in range(len(std)):
            if std[i] == ans[i]:
                check[i] = ans[i] + ' '
                tot+=5
            else:
                check[i] = ans[i] + '*'
        
        temp.append(f'{no:>4}   {"".join(check)}   {tot:>6}\n')
    temp[-1] = temp[-1].strip()
    
    outfile.writelines(temp)