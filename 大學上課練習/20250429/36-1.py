from datetime import datetime
class Rental:
    def __init__(self, model,rdate):
        self.model = model
        self.rdate = rdate
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,model):
        self.__model = model

    @property
    def rdate(self):
        return self.__rdate
    @rdate.setter
    def rdate(self,rdate):
        self.__rdate = rdate

    def price(self):
        tdate = datetime.strptime(self.__rdate, '%Y/%m/%d')
        w = tdate.weekday()
        if self.model == "A":
            if 0 <= w <= 4:
                return 2000
            else:
                return 2500
        elif self.model == "B":
            if 0 <= w <= 4:
                return 1800
            else:
                return 2100
        else:
            if 0 <= w <= 4:
                return 1500
            else:
                return 1900

class InsuranceRental(Rental):
    def __init__(self, model,rdate,types):
        super().__init__(model,rdate)
        self.__types = types
    @property
    def types(self):
        return self.__types
    @types.setter
    def types(self,types):
        self.__types = types
    def price(self):
        base = super().price()
        if self.types == "F":
            return base + 800
        else:
            return base + 500

s1 = Rental("A","2024/5/16")
s2 = Rental("A","2024/5/18")
s3 = Rental("B","2024/5/16")
s4 = Rental("B","2024/5/18")
s5 = Rental("C","2024/5/16")
s6 = Rental("C","2024/5/18")
print(s1.price())
print(s2.price())
print(s3.price())
print(s4.price())
print(s5.price())
print(s6.price())

h1 = InsuranceRental("A","2024/5/16","F")
h2 = InsuranceRental("A","2024/5/18","H")
h3 = InsuranceRental("B","2024/5/16","F")
h4 = InsuranceRental("B","2024/5/18","H")
h5 = InsuranceRental("C","2024/5/16","F")
h6 = InsuranceRental("C","2024/5/18","H")
print(h1.price())
print(h2.price())
print(h3.price())
print(h4.price())
print(h5.price())
print(h6.price())
