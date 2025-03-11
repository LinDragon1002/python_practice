with open ('card.csv','r', encoding='utf-8') as infile, open ('out.csv','w', encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]
    
    temp = []
    std = 'BCDADABCDBAABCADCBDC'
    
    for d in data:
        no, ans = d.split(',')
        
        tot = 0
        for i in range(len(std)):
            if std[i] == ans[i] and i % 2 == 0:
                tot+=3
            elif std[i] == ans[i] and i % 2 != 0:
                tot+=7
        
        temp.append(f'{no:>4}號  {tot:>3}分\n')
    temp[-1] = temp[-1].strip()
    
    outfile.writelines(temp)