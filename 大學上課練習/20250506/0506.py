from abc import ABC, abstractmethod
# 定義一個抽象類別 Employee
class Employee(ABC):
    def __init__(self, name, years):
        self.name = name
        self.years = years
    @property
    def name(self):
        return self.__name
    @property
    def years(self):
        return self.__years
    @name.setter
    def name(self,name):
        self.__name = name
    @years.setter
    def years(self,years):
        self.__years = years
    # 抽象方法
    @abstractmethod
    def slary(self):
        NotImplemented

class RegularEmployee(Employee):
    def __init__(self, name,years,rank):
        super().__init__(name,years)
        self.rank = rank
        # self.name = name
        # self.years = years
    # @property
    # def name(self):
    #     return self.__name
    @property
    def rank(self):
        return self.__rank

    # @name.setter
    # def name(self,name):
    #     self.__name = name
    @rank.setter
    def rank(self,rank):
        self.__rank = rank

    def slary(self):
        if self.rank == "A":
            return 50000 + 1500 * super().years
        elif self.rank == "B":
            return 40000 + 1500 * super().years
        else:
            return 30000 + 1500 * super().years

class ParttimeEmployee(Employee):
    def __init__(self, name,years,hour):
        super().__init__(name,years)
        self.hour = hour
        # self.name = name
        # self.years = years
    # @property
    # def name(self):
    #     return self.__name
    @property
    def hour(self):
        return self.__hour

    # @name.setter
    # def name(self,name):
    #     self.__name = name
    @hour.setter
    def hour(self,hour):
        self.__hour = hour

    def slary(self):
            return 250 * self.hour + 850 * super().years
class OverseaEmployee(Employee):
    def __init__(self, name, years,country):
        super().__init__(name, years)
        self.country = country
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self,country):
        self.__country = country
    def slary(self):
        if self.country == "日本":
            return 80000 + 1850 * super().years
        elif self.country == "美國":
            return 100000 + 2250 * super().years
class ProjectEmployee(Employee):
    def __init__(self, name, years,total):
        super().__init__(name, years)
        self.total = total
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self,total):
        self.__total = total
    def slary(self):
        if super().years >= 5:
            return self.total * 0.08
        else:
            return self.total * 0.05

employee = []

# employee.append(RegularEmployee("王小名",5,"A"))
# employee.append(RegularEmployee("李小明",3,"B"))
# employee.append(RegularEmployee("陳小華",1,"C"))

# employee.append(ParttimeEmployee("林小名",5, 20))
# employee.append(ParttimeEmployee("葉小明",3, 30))
# employee.append(ParttimeEmployee("李小華",1, 40))

employee.append(OverseaEmployee("王小名",5,"日本"))
employee.append(OverseaEmployee("陳小華",3,"美國"))
employee.append(ProjectEmployee("王小名",3,1000000))
employee.append(ProjectEmployee("陳小華",4,1250000))

for e in employee:
    print(e.slary())
