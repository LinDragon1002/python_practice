'''
撰寫一個函式完成以下要求:

1. 函式名稱: compute_total
2. 功能: 計算租車費用
3. 傳入參數: 
   (1) 車型 (參數自訂, 接收一個文字)  
   (2) 租用天數 (參數名稱:days, 接收一個整數, 內定值為1)
   (3) 是否加購保險 (參數名稱:insurance, 接收一個布林, 內定值為False)  
4. 租車總金額計算方式:
   (1) 基本費用
       若車型是 A、C、D、K 其中之一, 每天收費3,500元
       若車型是 B、F、G、M 其中之一, 每天收費2,500元
       若非以上車型, 每天收費1,500元
       
       基本費用 = 每日收費*租用天數
       
   (2) 保險費用
       (A) 如果「有」加購保險, 依以下方式計算保險費:
           若車型是 A、C、D、K 其中之一, 每天保費1,500元
           若車型是 B、F、G、M 其中之一, 每天保費800元
           若非以上車型, 每天保費450元
       
           保險費用 = 每天保費*租用天數
               
       (B) 如果「沒有」加購保險, 保險費用=0
       
   (3) 租車費用
       租車費用 = 基本費用 + 保險費用
                   
   (4) 回傳「租車費用」      
'''
#(寫下你的函式)
def compute_total(types,days=1,insurance=False):
    if types in ("A","C","D","K"):
        free = 3500
    elif types in ("B","F","G","M"):
        free = 2500
    else:
        free = 1500

    basefree = days * free

    if insurance:
        if types in ("A","C","D","K"):
            tax = 1500
        elif types in ("B","F","G","M"):
            tax = 800
        else:
            tax = 450
    else:
        tax = 0
    basetax = days * tax

    return basefree + basetax

    


#===============================
#主程式, 已完成, 不必修改
#===============================
print(f'{compute_total("A"):,}元')
print(f'{compute_total("D"):,}元')
print(f'{compute_total("F"):,}元')
print(f'{compute_total("H"):,}元')
print(f'{compute_total("C",days=3,insurance=True):,}元')
print(f'{compute_total("K",days=2,insurance=True):,}元')
print(f'{compute_total("G",days=4,insurance=True):,}元')
print(f'{compute_total("T",days=4,insurance=True):,}元')
#===============================

'''
參考解答:
3,500元
3,500元
2,500元
1,500元
15,000元
10,000元
13,200元
7,800元
'''