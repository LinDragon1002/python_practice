class std:
    def __init__(self,no,name):
        self.no = no # 這裡會呼叫no的setter
        self.name = name

    @property # 這是屬性裝飾器，讓我們可以用get_no()來取得__no的值
    def no(self):
        return self.__no
    @property
    def name(self):
        return self.__name

    @no.setter # 這是屬性裝飾器，讓我們可以用no = 85來設定__no的值
    def no(self,no):
        self.__no = no

    @name.setter
    def name(self,name):
        self.__name = name

s1 = std(11256001,"王小明")
s2 = std(11256002,"陳小華")
print(s1.no,s1.name,sep="\n")
print(s2.no,s2.name,sep="\n")