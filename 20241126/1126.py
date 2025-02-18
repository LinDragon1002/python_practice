with open ('card.csv','r') as infile, open ('out.csv','w') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]
    
    temp = []
    std = 'BCDADABCDBAABCADCBDC'
    
    for d in data:
        no, ans = d.split(',')
        
        tot = 0
        check = [None]*20
        
        # for i in range(len(std)):
        #     if std[i] == ans[i]:
        #         tot+=5
                
        # for i in range(len(std)):
        #     if std[i] == ans[i] and i<=9:
        #         tot+=2
        #     elif std[i] == ans[i] and i>=10:
        #         tot+=8
                
        for i in range(len(std)):
            if std[i] == ans[i]:
                check[i] = ' '
                tot+=5
            else:
                check[i] = '*'
        
        temp.append(f'{no:>4}   {"".join(check)}   {tot:>3}\n')

        
        # " ".join(ans) 為合併前面字串加入到ans裡面
        # temp.append(f'{no:>4}   {" ".join(ans)}   {tot:>3}\n')
        
    temp[-1] = temp[-1].strip()
    
    outfile.writelines(temp)