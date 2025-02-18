# with open ('iris.csv','r',encoding='utf-8') as infile:
#     data = infile.readlines()
#     data = [n.strip() for n in data]

#     total = [0]*4
#     cnt = 0

#     for i in data:
#         s_len, s_wid, p_len, p_wid, spe = i.split(",")

#         #轉型(casting)
#         # map(型態, list裡面的變數)
#         s_len, s_wid, p_len, p_wid = map(float, [s_len, s_wid, p_len, p_wid])
#         # total = s_len + s_wid + p_len + p_wid
#         # counting = round(sum(map(float, [s_len, s_wid, p_len, p_wid])), 2)

#         total[0] += s_len
#         total[1] += s_wid
#         total[2] += p_len
#         total[3] += p_wid
#         cnt += 1

#     for i in range(4):
#         avg = round(total[i]/cnt,2)
#         print(avg)

#     print(sorted(total.items(), key=lambda x:x[0],reverse=True))

#     for i in sorted(total.items(), key=lambda x:x[0],reverse=True):
#         print(f'{i[0]}:有{i[1]}個')

# with open ('iris.csv','r',encoding='utf-8') as infile:
#     data = infile.readlines()
#     data = [n.strip() for n in data]

#     total = [[0]*4 for _ in range(3)]
#     cnt = [0]*3

#     for i in data:
#         s_len, s_wid, p_len, p_wid, spe = i.split(",")
#         s_len, s_wid, p_len, p_wid = map(float, [s_len, s_wid, p_len, p_wid])

#         m = {'山鳶尾花':0,'變色鳶尾花':1,'維吉尼亞鳶尾花':2}
#         total[m[spe]][0] += s_len
#         total[m[spe]][1] += s_wid
#         total[m[spe]][2] += p_len
#         total[m[spe]][3] += p_wid
#         cnt[m[spe]] += 1

#     for i in range(3):
#         avg = []
#         for j in range(4):
#             avg.append(round(total[i][j]/cnt[i],2))
#         print(*avg)

# with open ('iris.csv','r',encoding='utf-8') as infile:
#     data = infile.readlines()
#     # data = [n.strip().split(",") for n in data]
#     # data = [[float(value) for value in row[:4]]+[row[4]] for row in data]
#     data = [[float(value) for value in n.strip().split(",")[:4]] + [n.strip().split(",")[4]] for n in data]


#     tot = [k[0] for k in data if k[4] == '山鳶尾花']
#     avg = sum(tot)/len(tot)
#     print(avg)


with open ('iris.csv','r',encoding='utf-8') as infile:
    data = infile.readlines()
    data = [[float(value) for value in n.strip().split(",")[:4]] + [n.strip().split(",")[4]] for n in data]
    m = ['山鳶尾花','變色鳶尾花','維吉尼亞鳶尾花']
    avg = [[0]*4 for _ in range(3)]
    for i in range(4):
        tot = [k[i] for k in data if k[4] == m[0]]
        avg[0][i] = round(sum(tot)/len(tot),2)
        # avg[0][i] = round(sum([k[i] for k in data if k[4] == m[0]])/len([k[i] for k in data if k[4] == m[0]]),2) # type: ignore
        avg[1][i] = round(sum([k[i] for k in data if k[4] == m[1]])/len([k[i] for k in data if k[4] == m[1]]),2) # type: ignore
        avg[2][i] = round(sum([k[i] for k in data if k[4] == m[2]])/len([k[i] for k in data if k[4] == m[2]]),2) # type: ignore
    for i in range(3):
        print(f'{m[i]} {" ".join(map(str, avg[i]))}')


# with open('iris.csv', 'r', encoding='utf-8') as infile:
#     data = [[float(value) for value in n.strip().split(",")[:4]] + [n.strip().split(",")[4]] for n in infile.readlines()]
#     flowers = ['山鳶尾花', '變色鳶尾花', '維吉尼亞鳶尾花']
#     avg = {flower: [round(sum(k[i] for k in data if k[4] == flower) / sum(1 for k in data if k[4] == flower), 2)for i in range(4)]for flower in flowers} # type: ignore
#     for flower in flowers:
#         print(f'{flower} {", ".join(map(str, avg[flower]))}')
