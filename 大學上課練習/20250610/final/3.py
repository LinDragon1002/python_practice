#=========================    
# 類別, 寫下你的程式
#=========================      




                 
                  
#=========================    
# 主程式, 已完成, 勿改
#=========================
data = []

data.append(DayEmployee('王小明', 170, 'A'))
data.append(DayEmployee('陳小華', 150, 'A'))
data.append(DayEmployee('張小文', 165, 'B'))
data.append(DayEmployee('王大明', 170, 'B'))
data.append(DayEmployee('陳大華', 150, 'C'))
data.append(DayEmployee('張大文', 165, 'C'))
data.append(NightEmployee('蔡小梅', 55, True, True))
data.append(NightEmployee('周小蓉', 60, True, False))
data.append(NightEmployee('黃小智', 65, False, True))
data.append(NightEmployee('黃小智', 75, False, False))

tot = [150000, 160000, 170000, 180000, 190000, 200000, 150000, 160000, 170000, 180000]

for i in range(len(data)):
    print(f'姓名:{data[i].name}, 薪水:{data[i].salary(tot[i]):,}元') 
    

#=========================
# 參考解答
#=========================
'''
姓名:王小明, 薪水:43,500元
姓名:陳小華, 薪水:42,800元
姓名:張小文, 薪水:40,700元
姓名:王大明, 薪水:42,300元
姓名:陳大華, 薪水:39,500元
姓名:張大文, 薪水:40,500元
姓名:蔡小梅, 薪水:24,875元
姓名:周小蓉, 薪水:23,500元
姓名:黃小智, 薪水:26,125元
姓名:黃小智, 薪水:25,875元
'''