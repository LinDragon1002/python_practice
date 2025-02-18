'''
三. 計算等級

1. 檔案
   (1) StudentsPerformance.csv
       內容依序為序號、宗教、父母教育程度、午餐、考試準備、數學、閱讀、寫作
              
   (2) out.csv
       輸出檔
       
2. 處理
   (1) 依序讀入檔案內的每筆記錄
   (2) 計算總分, 總分 = 數學 + 閱讀 + 寫作
   (3) 如果250<=總分, 等級為A
       如果230<=總分<=249, 等級為B
       如果200<=總分<=229, 等級為C
       如果總分<=199, 等級為D
                     
3. 輸出
   (1) 序號
   (2) 加權總分 (不必設定輸出格式)
   (3) 等級 (不必設定輸出格式)

4. 參考解答   
序號1的總分218, 等級為C
序號2的總分247, 等級為B
序號3的總分278, 等級為A
序號4的總分148, 等級為D
序號5的總分229, 等級為C
序號6的總分232, 等級為B
序號7的總分275, 等級為A
序號8的總分122, 等級為D
'''
with open('StudentsPerformance.csv', 'r', encoding='utf-8') as infile, open('out.csv', 'w', encoding='utf-8') as outfile:
    data = infile.readlines()
    data = [line.strip() for line in data]

    for line in data:
        no,*_,math,reading,writing = line.split(',')
        total = int(math) + int(reading) + int(writing)
        if total >= 250:
            level = 'A'
        elif 230 <= total <= 249:
            level = 'B'
        elif 200 <= total <= 229:
            level = 'C'
        elif total <= 199:
            level = 'D'
        outfile.write(f'序號{no}的總分{total}, 等級為{level}\n')