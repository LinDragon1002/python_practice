#=========================    
# 類別, 寫下你的程式
#=========================      
from datetime import datetime
class Customer:
    def __init__(self,name,date,person):
        self.name = name
        self.date = date
        self.person = person
    @property
    def name(self):
        return self.__name
    @property
    def date(self):
        return self.__date
    @property
    def person(self):
        return self.__person
    @name.setter
    def name(self,name):
        self.__name = name
    @date.setter
    def date(self,date):
        self.__date = date
    @person.setter
    def person(self,person):
        self.__person = person
    def price(self):
        tdate = datetime.strptime(self.date, '%Y-%m-%d')
        w = tdate.weekday()
        if 0 <= w <= 4:
            price = 860
        else:
            price = 1050
        return int((price * self.person) * 1.1)
class VIPCustomer(Customer):
    def __init__(self,name,date,person,wine):
        super().__init__(name,date,person)
        self.wine = wine
    @property
    def wine(self):
        return self.__wine
    @wine.setter
    def wine(self,wine):
        self.__wine = wine
    def price(self):
        base = super().price()
        if self.wine == "A":
            return base + self.person * 550
        else:
            return base + self.person * 400
#=========================    
# 主程式, 已完成, 勿改
#=========================
data = []
data.append(Customer('王小明', '2024-5-18', 2))
data.append(Customer('陳小華', '2024-5-20', 4))
data.append(Customer('張小文', '2024-5-19', 3))
data.append(VIPCustomer('蔡小梅', '2024-5-18', 2, 'A'))
data.append(VIPCustomer('周小蓉', '2024-5-20', 4, 'B'))
data.append(VIPCustomer('黃小智', '2024-5-19', 3, 'A'))

for d in data:
    print(f'姓名:{d.name}, 價格:{d.price():,}元')  


#=========================
# 參考解答
#=========================
'''
姓名:王小明, 價格:2,310元
姓名:陳小華, 價格:3,784元
姓名:張小文, 價格:3,465元
姓名:蔡小梅, 價格:3,410元
姓名:周小蓉, 價格:5,384元
姓名:黃小智, 價格:5,115元
'''