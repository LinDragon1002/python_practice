with open ('card.csv','r', encoding='utf-8') as infile, open ('out.csv','w', encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [i.strip() for i in data]
    
    cnt = {i:0 for i in range(0, 101, 5)}
    std = 'BCDADABCDBAABCADCBDC'
    
    for d in data:
        no, ans = d.split(',')
        
        tot = 0

        for i in range(len(std)):
            if std[i] == ans[i]:
                tot+=5
                
        
        cnt[tot]+=1
        
    
    for key in cnt:
        print(f'{key}分: {cnt[key]}人')