#=========================    
# 類別, 寫下你的程式
#=========================   
from abc import ABC, abstractmethod
# 定義一個抽象類別 Employee
class Employee(ABC):
    def __init__(self, name, department):
        self.name = name
        self.department = department
    @property
    def name(self):
        return self.__name
    @property
    def department(self):
        return self.__department
    @name.setter
    def name(self,name):
        self.__name = name
    @department.setter
    def department(self,department):
        self.__department = department
    # 抽象方法
    @abstractmethod
    def salary(self):
        return NotImplemented

class DayEmployee(Employee):
    def __init__(self, name,department):
        super().__init__(name,department)

    def salary(self,hours):
        if self.department == "資訊部":
            return 80000 + 300 * hours
        elif self.department == "會計部":
            return 75000 + 300 * hours
        else:
            return 70000 + 300 * hours
class NightEmployee(Employee):
    def __init__(self, name,department,outside):
        super().__init__(name,department)
        self.outside = outside
    @property
    def outside(self):
        return self.__outside
    @outside.setter
    def outside(self,outside):
        self.__outside = outside

    def salary(self,hours):
        if self.department == "資訊部":
            if self.outside:
                return 55000 + 350 * hours + 10000
            else:
                return 55000 + 350 * hours
        else:
            if self.outside:
                return 45000 + 350 * hours + 10000
            else:
                return 45000 + 350 * hours

#=========================    
# 主程式, 已完成, 勿改
#=========================
data = []
data.append(DayEmployee('王小明', '資訊部'))
data.append(DayEmployee('陳小華', '會計部'))
data.append(DayEmployee('張小文', '生產部'))
data.append(NightEmployee('蔡小梅', '資訊部', True))
data.append(NightEmployee('周小蓉', '會計部', False))
data.append(NightEmployee('黃小智', '生產部', True))

hours = [1, 2, 3, 3, 2, 1]

for i in range(6):
    print(f'姓名:{data[i].name}, 薪水:{data[i].salary(hours[i]):,}元')  


#=========================
# 參考解答
#=========================
'''
姓名:王小明, 薪水:80,300元
姓名:陳小華, 薪水:75,600元
姓名:張小文, 薪水:70,900元
姓名:蔡小梅, 薪水:66,050元
姓名:周小蓉, 薪水:45,700元
姓名:黃小智, 薪水:55,350元
'''