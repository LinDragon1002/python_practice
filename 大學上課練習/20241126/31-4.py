with open ('card.csv','r', encoding='utf-8') as infile, open ('out.csv','w', encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]
    
    temp = []
    std = 'BCDADABCDBAABCADCBDC'
    
    for d in data:
        no, ans = d.split(',')
        
        tot = 0
        for i in range(len(std)):
            if std[i] == ans[i]:
                tot+=5
        if tot == 100:
            grades = 5
        elif 80<=tot<=99:
            grades = 4
        elif 60<=tot<=79:
            grades = 3
        elif 40<=tot<=59:
            grades = 2
        elif 20<=tot<=39:
            grades = 1
        elif 0<=tot<=19:
            grades = 0
        
        temp.append(f'{no:>4}號 {grades:>2}級分\n')
    temp[-1] = temp[-1].strip()
    
    outfile.writelines(temp)