with open ('card.csv','r', encoding='utf-8') as infile, open ('out.csv','w', encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]
    
    people = {"及格":0,"不及格":0}
    std = 'BCDADABCDBAABCADCBDC'
    
    for d in data:
        no, ans = d.split(',')
        
        tot = 0

        for i in range(len(std)):
            if std[i] == ans[i]:
                tot+=5
                
        if tot >= 60:
            people['及格']+=1
        else:
            people['不及格']+=1
        
    
    for key in people:
        print(f'{key}人數: {people[key]}')