#=========================    
# 類別, 寫下你的程式
#=========================  




         
                   
#=========================    
# 主程式, 已完成, 勿改
#=========================
data1 = []
data2 = []

data1.append(Customer('王小明', '2024-5-17', 2))
data1.append(Customer('陳小華', '2024-5-18', 4))
data1.append(Customer('張小文', '2024-5-19', 3))
data1.append(Customer('楊小雅', '2024-5-20', 1))
data2.append(VIPCustomer('蔡小梅', '2024-5-17', 2, '1'))
data2.append(VIPCustomer('周小蓉', '2024-5-18', 4, '2'))
data2.append(VIPCustomer('黃小智', '2024-5-19', 3, '1'))
data2.append(VIPCustomer('朱小芬', '2024-5-20', 1, '2'))
data2.append(VIPCustomer('蔡大梅', '2024-5-17', 2, '1'))
data2.append(VIPCustomer('周大蓉', '2024-5-18', 4, '2'))
data2.append(VIPCustomer('黃大智', '2024-5-19', 3, '1'))
data2.append(VIPCustomer('朱大芬', '2024-5-20', 1, '2'))

style1 = ['A', 'B', 'C', 'D']
style2 = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
wine2 = [True, False, True, False, True, False, True, False]

for i in range(len(data1)):
    print(f'姓名:{data1[i].name}, 價格:{data1[i].price(style1[i]):,}元')  

for i in range(len(data2)):
    print(f'姓名:{data2[i].name}, 價格:{data2[i].price(style2[i], wine2[i]):,}元')  

#=========================
# 參考解答
#=========================
'''
姓名:王小明, 價格:2,500元
姓名:陳小華, 價格:4,400元
姓名:張小文, 價格:2,400元
姓名:楊小雅, 價格:600元
姓名:蔡小梅, 價格:2,600元
姓名:周小蓉, 價格:4,860元
姓名:黃小智, 價格:3,300元
姓名:朱小芬, 價格:720元
姓名:蔡大梅, 價格:1,880元
姓名:周大蓉, 價格:3,240元
姓名:黃大智, 價格:2,820元
姓名:朱大芬, 價格:540元
'''