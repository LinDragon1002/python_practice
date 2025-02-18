'''
一. 計算加權總分

1. 檔案
   (1) ntub.csv
       內容依序為序號、入學方式、錄取科別、作文、國文、英文、數學、社會、自然
              
   (2) out.csv
       輸出檔
       
2. 處理
   (1) 依序讀入檔案內的每筆記錄
   (2) 計算加權總分, 加權總分 = 國文 + 英文*1.5 + 數學*2
   
3. 輸出
   (1) 序號
   (2) 加權總分 (不必設定輸出格式)

4. 參考解答   
   序號1的加權總分222.0
   序號2的加權總分185.5
   序號3的加權總分248.0
   序號4的加權總分208.5
   序號4的加權總分204.5
   序號6的加權總分201.0
   序號7的加權總分170.5
   序號8的加權總分201.0
'''
with open('ntub.csv', 'r', encoding='utf-8') as infile, open('out.csv', 'w') as outfile:
   data = infile.readlines()
   data = [line.strip() for line in data]

   for line in data:
      data = line.split(',')
      no = data[0]
      chinese = int(data[4])
      english = int(data[5])
      math = int(data[6])
      total = chinese + english*1.5 + math*2
      print(f'序號{no}的加權總分{total}')

      outfile.write(f'序號{no}的加權總分{total}\n')