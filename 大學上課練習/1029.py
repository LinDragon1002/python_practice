# with open('ntub.csv', 'r', encoding='utf-8') as infile, \
#     open('out.csv','w',encoding='utf-8') as outfile:
#     data = infile.readlines()

#     out = []

#     for row in data:
#         gender, _, dept, *scores = row.strip().split(',')
#         total = sum([int(i) for i in scores])

#         out.append(f'{gender},{dept},{total}\n')    #將資料加入輸出暫存

#     out[-1] = out[-1].strip()                       #去除最後一筆的跳行
#     print(out)

#     outfile.writelines(out)                         #將暫存內容寫到out.csv

with open('StudentsPerformance.csv', 'r', encoding='utf-8') as infile, \
    open('out1.csv','w',encoding='utf-8') as outfile:
    data = infile.readlines()

    out = []

    for row in data:
        sex, _, edu, lunch, _, *scores = row.strip().split(',')
        total = sum([int(i) for i in scores])

        out.append(f'{sex},{edu},{lunch},{total}\n')    #將資料加入輸出暫存

    out[-1] = out[-1].strip()                       #去除最後一筆的跳行
    print(out)

    outfile.writelines(out)                         #將暫存內容寫到out.csv