'''
一. 計算點數

1. 檔案
   (1) ntub.csv
       內容依序為序號、入學方式、錄取科別、作文、國文、英文、數學、社會、自然
              
   (2) out.csv
       輸出檔
       
2. 處理
   (1) 依序讀入檔案內的每筆記錄
   (2) 如果國文==60, 可得3點 
       如果50<=國文<=59, 可得2點  
       如果40<=國文<=49, 可得1點 
       如果國文<=39, 可得0點
   (3) 如果英文==60, 可得3點 
       如果50<=英文<=59, 可得2點  
       如果40<=英文<=49, 可得1點 
       如果英文<=39, 可得0點   
   (4) 計算總點數, 總點數 = 國文點數 + 英文點數
   
3. 輸出
   (1) 序號
   (2) 總點數

4. 參考解答   
   序號1的總點數4
   序號2的總點數3
   序號3的總點數3
   序號4的總點數2
   序號5的總點數3
   序號6的總點數3
   序號7的總點數1
   序號8的總點數4
'''
with open('ntub.csv','r',encoding='utf-8') as infile, open('out.csv','w',encoding='utf-8')as outfile:
    data = infile.readlines()
    data = [line.strip() for line in data]

    for line in data:
        score = [0]*10
        no,_,_,_,chi,eng,*_= line.split(',')
        score[int(chi)//10-1] += 1
        score[int(eng)//10-1] += 1
        point = score[5]*3 + score[4]*2 + score[3]*1
        outfile.write(f'序號{no}的總點數{point}\n')
