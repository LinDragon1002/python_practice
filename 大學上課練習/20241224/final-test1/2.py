'''
二. 計算總分

1. 檔案
   (1) card.csv
       內容依序為序號、考生答案
              
   (2) out.csv
       輸出檔
       
2. 處理
   (1) 正確答案: ECDADAECDBAABCADCBDC
   (2) 依序讀入檔案內的每筆記錄
   (3) 依序比對考生答案及標準答案, 
       若考生答案和標準答案相同可得5分,
       否則, 若標準答案為E, 考生答案為B或C也可得5分       
   (4) 總分 = 累計20題的得分
   
3. 輸出
   (1) 序號
   (2) 總分

4. 參考解答   
   序號1的總分100
   序號2的總分35
   序號3的總分65
   序號4的總分70
   序號5的總分100
   序號6的總分60
   序號7的總分95
   序號8的總分90
'''
with open ('card.csv','r',encoding='utf-8') as infile,open ('out.csv','w',encoding='utf-8')as outfile:
   data = infile.readlines()
   data = [line.strip() for line in data]
   Ans = "ECDADAECDBAABCADCBDC"
   total = 0

   for line in data:
      no,ans = line.split(',')
      for i in range(len(Ans)):
         if Ans[i] == ans[i]:
            total += 5
         elif Ans[i] == 'E' and ans[i] =='B' or ans[i] =='C' and Ans[i] == 'E':
            total += 5
      outfile.write(f'序號{no}的總分{total}\n')
      total = 0