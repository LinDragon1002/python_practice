'''
--------Employee ---------
<<get/set>> - rank: int
<<get/set>> - overhours: int
----------------------
+ 建構元(rank,overhours)
+ salary(): int

-> extends ExpatEmployee
-> extends projectEmployee

'''

# 父類別
class Employee:
    def __init__(self,rank,overhours):
        self.rank = rank
        self.overhours = overhours

    # 這是屬性裝飾器，讓我們可以用get_rank()來取得__rank的值
    @property
    def rank(self):
        return self.__rank
    @property
    def overhours(self):
        return self.__overhours

    # 這是屬性裝飾器，讓我們可以用rank = 85來設定__rank的值
    @rank.setter
    def rank(self,rank):
        self.__rank = rank
    @overhours.setter
    def overhours(self,overhours):
        self.__overhours = overhours

    def salary(self):
        # 呼叫getter取值
        if self.rank == "A":
            return 50000 + self.overhours * 500
        else:
            return 40000 + self.overhours * 400

# 繼承
# 子類別
class ExpatEmployee(Employee):
    def __init__(self,rank,overhours,city):
        # 呼叫父類別的建構元
        super().__init__(rank,overhours)
        self.city = city
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self,city):
        if city in ["台中","高雄"]:
            self.__city = city
        else:
            raise ValueError("城市錯誤")

    def salary(self):
        # 呼叫父類別的salary()方法
        base = super().salary()
        if self.city == "台中":
            return base + 5000
        else:
            return base + 8000

class projectEmployee(Employee):
    def __init__(self,rank,overhours,total):
        super().__init__(rank,overhours)
        self.total = total
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self,total):
        self.__total = total
    def salary(self):
        base = super().salary()
        return base + self.total * 0.05

s1 = Employee("A",5)
s2 = Employee("B",10)
s3 = ExpatEmployee("A",5, "台中")
s4 = ExpatEmployee("B",10,"高雄")
s5 = projectEmployee("A",5,100000)
s6 = projectEmployee("B",10,200000)
# print(s1.salary())
# print(s2.salary())
# print(s3.salary())
# print(s4.salary())
# print(s5.salary())
# print(s6.salary())


from datetime import datetime

class Rental:
    def __init__(self, rdate):
        self.__rdate = rdate

    def price(self):
        tdate = datetime.strptime(self.__rdate, '%Y/%m/%d')
        w = tdate.weekday()
        if 0 <= w <= 4:
            return 800
        elif w == 5:
            return 1200
        else:
            return 1000

r1 = Rental("2025/4/27")
print(r1.price())