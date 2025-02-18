'''
二. 計算奇數個數

1. 檔案
   (1) lotto.csv
       內容依序為序號、簽注號碼1、號碼2、號碼3、號碼4、號碼5、號碼6
              
   (2) out.csv
       輸出檔
       
2. 處理
   (1) 依序讀入檔案內的每筆記錄
   (2) 計算每筆記錄的六個簽注號碼中, 有幾個是「奇數」? 
   
3. 輸出
   (1) 序號
   (2) 有幾個「奇數」

4. 參考解答   
   序號1有3個奇數
   序號2有1個奇數
   序號3有4個奇數
   序號4有3個奇數
   序號5有4個奇數
   序號6有3個奇數
   序號7有2個奇數
   序號8有6個奇數
'''
with open('lotto.csv', 'r', encoding='utf-8') as infile, open('out.csv','w',encoding='utf-8') as outfile:
   data = infile.readlines()
   data = [line.strip() for line in data]

   for line in data:
      ans = 0
      no,*items = line.split(',')
      for i in range(len(items)):
         if int(items[i]) % 2 == 1:
            ans += 1
      outfile.write(f'序號{no}有{ans}個奇數\n')