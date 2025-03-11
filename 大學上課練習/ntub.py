#開檔案    檔名       讀入 編碼
with open('ntub.csv','r', encoding='utf-8') as infile:
    data = infile.readlines()         #讀入所有資料
    data = [i.strip() for i in data]   #去除\n
    data2 = []
    for row in data:                   #逐一取出
        # row = row.split(',')           #split切割
        gender, enroll, dept, lec, chi, eng, mat, soc, nat = row.split(',')  #可以寫成 gneder, enroll, *_(表示後面的不會用到就直接這樣寫) = row.split(',')
        scores = [lec, chi, eng, mat, soc, nat]
        scores = [int(i) for i in scores]
        data2.append([gender, enroll, sum(scores)])
        data2 = sorted(data2, key=lambda x:x[2], reverse=True)
        # total = lec + chi + eng + mat + soc + nat

    for gender, enroll, scores in data2:
        # print(gender, enroll, scores)
        print(f'{gender:^10}{enroll:^10}{scores:^10}')     #^10為置中
