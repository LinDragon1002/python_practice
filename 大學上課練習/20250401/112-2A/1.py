'''
撰寫一個函式完成以下要求:
1. 函式名稱: compute_total
2. 功能: 計算音樂會單人票總金額
3. 傳入參數: 
   (1) 座位區域 (參數自訂, 接收一個字串)  
   (2) 是否參加茶會 (參數名稱:party, 接收一個布林, 內定值為True)  
4. 音樂會單人票總金額計算方式:
   (1) 入場金額
       若座位區域為 'A', 入場金額 2,500元
       若座位區域為 'B', 入場金額 2,000元
       若座位區域為 'C', 入場金額 1,500元
       其他座位區域, 入場金額 1,000元
   (2) 茶會金額
       若參加茶會(True), 茶會金額600元; 若不參加(False), 免收茶會金額
   (3) 稅前金額
       稅前金額 = 入場金額 + 茶會金額
   (4) 總金額(四捨五入至整數)
       若稅前金額 >= 2000, 總金額 = 稅前金額 * 1.05
       否則, 總金額 = 稅前金額 * 1.02            
   (5) 回傳「總金額」      
'''
#(寫下你的函式)
def compute_total(area,party=True):
    if area == "A":
        expend = 2500
    elif area == "B":
        expend = 2000
    elif area == "C":
        expend = 1500
    else:
        expend = 1000
    if party:
        expend += 600
    if expend >= 2000:
        return int(expend * 1.05)
    else:
        return int(expend * 1.02)



#===============================
#主程式, 已完成, 不必修改
#===============================
print(f'{compute_total("A"):,}元')
print(f'{compute_total("B", party=False):,}元')
print(f'{compute_total("C", party=False):,}元')
print(f'{compute_total("D"):,}元')
print(f'{compute_total("A", party=False):,}元')
#===============================

#參考解答
'''
3,255元
2,100元
1,530元
1,632元
2,625元
'''