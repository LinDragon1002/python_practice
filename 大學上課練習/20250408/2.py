'''
撰寫一個函式完成以下要求:

1. 函式名稱: compute_score
2. 功能: 判斷是否及格
3. 傳入參數: 
   (1) 不定個數的「檢定分數」  (參數名稱自訂, 接收不定個數的整數)
4. 判斷是否及格的條件:
   (1) 符合以下任何條件, 判斷為及格, 否則為不及格
       (1-1) 在所有的檢定分數中, 「超過(含) 60 分」至少有4個 
       (1-2) 在所有的檢定分數中, 「超過(含) 70 分」至少有3個     
       (1-3) 在所有的檢定分數中, 「超過(含) 80 分」至少有2個                 
       (1-4) 在所有的檢定分數中, 「超過(含) 90 分」至少有1個   
              
   (2) 若及格, 回傳True
       否則回傳False    
'''
#(寫下你的函式)
def compute_score(*scores):
    temp = [0,0,0,0]
    for i in scores:
        if i >= 60:
            temp[0] += 1
        if i >= 70:
            temp[1] += 1
        if i >= 80:
            temp[2] += 1
        if i >= 90:
            temp[3] += 1
    if temp[0] >= 4 or temp[1] >= 3 or temp[2] >= 2 or temp[3] >= 1:
        return True
    return False




#===============================
#主程式, 已完成, 不必修改
#===============================
print(f'{compute_score(60, 50, 70, 50, 65)}')  
print(f'{compute_score(90, 80)}')
print(f'{compute_score(63, 25, 80, 10, 60)}')
print(f'{compute_score(70, 10, 75, 50, 45, 25, 80)}')
print(f'{compute_score(35, 45, 60, 70)}')
print(f'{compute_score(35, 65, 70, 60, 66)}')
print(f'{compute_score(100)}')
print(f'{compute_score(60, 60, 60, 50, 50, 50, 50, 50, 50)}')
#===============================

'''
參考解答:
False
True
False
True
False
True
True
False
'''