'''
三. 計算金額

1. 檔案
   (1) cake.csv
       內容依序為序號、50項商品的購買數量
              
   (2) out.csv
       輸出檔
       
2. 處理
   (1) 依序讀入檔案內的每筆記錄
   (2) 前25項商品每個80元; 後25項商品每個95元     
   (3) 計算總金額
   
3. 輸出
   (1) 序號
   (2) 總金額 (千分位符號)

4. 參考解答   
   序號1的總金額480元
   序號2的總金額635元
   序號3的總金額810元
   序號4的總金額1,115元
   序號5的總金額1,005元
   序號6的總金額765元
   序號7的總金額765元
   序號8的總金額845元
'''
with open ('cake.csv','r',encoding='utf-8') as infile, open ('out.csv','w', encoding='utf-8')as outfile:
   data = infile.readlines()
   data = [line.strip() for line in data]
   total =0

   for line in data:
      no, *items = line.split(',')
      for i in range(len(items)):
         if i <= 24:
            total += int(items[i])*80
         elif i > 24:
            total += int(items[i])*95
      outfile.write(f'序號{no}的總金額{total:,.0f}元\n')
      total = 0