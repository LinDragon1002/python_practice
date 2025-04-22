class Parttime:
    def __init__(self,years,hours):
        self.years = years # 這裡會呼叫years的setter
        self.hours = hours

    @property # 這是屬性裝飾器，讓我們可以用get_years()來取得__years的值
    def years(self):
        return f'年資:{self.__years}'
    @property
    def hours(self):
        return f'工時:{self.__hours}'

    @years.setter # 這是屬性裝飾器，讓我們可以用years = 85來設定__years的值
    def years(self,years):
        self.__years = years

    @hours.setter
    def hours(self,hours):
        self.__hours = hours

    def salary(self):
        if self.__years >= 5:
            return f'薪水:{self.__hours * 350:,}元'
        return f'薪水:{self.__hours * 245:,}元'

s1 = Parttime(5,128)
s2 = Parttime(3,95)

print(s1.years,s1.hours,s1.salary(),sep=",")
print(s2.years,s2.hours,s2.salary(),sep=",")