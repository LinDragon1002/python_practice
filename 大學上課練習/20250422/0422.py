class Score:
    def __init__(self,chi,eng):
        self.chi = chi
        self.eng = eng

    def total(self):
        return self.chi + self.eng

# 生成物件
s1 = Score(90,80)
# 呼叫方法
print(s1.total())

# 更改物件的屬性
s1.eng = 85
print(s1.total())

# 私用屬性(private)
class Score2:
    def __init__(self,chi,eng):
        self.__chi = chi
        self.__eng = eng

    def set_chi(self,chi):self.__chi = chi
    def set_eng(self,eng):self.__eng = eng

    def total(self):
        return self.__chi + self.__eng

# 生成物件
s1 = Score2(90,80)
# 呼叫方法
print(s1.total())
print(s1.__chi) # 會報錯，因為__chi是私有屬性
s1.set_chi(85)

# 在setter加入檢查程序
class Score3:
    def __init__(self,chi,eng):
        self.chi = chi # 這裡會呼叫chi的setter
        self.eng = eng

    @property # 這是屬性裝飾器，讓我們可以用get_chi()來取得__chi的值
    def chi(self):
        return self.__chi
    @property
    def eng(self):
        return self.__eng

    @chi.setter # 這是屬性裝飾器，讓我們可以用chi = 85來設定__chi的值
    def chi(self,chi):
        if 0 <= chi <= 100:
            self.__chi = chi
        else:
            raise ValueError('國文分數有錯')

    @eng.setter
    def eng(self,eng):
        if 0 <= eng <= 100:
            self.__eng = eng
        else:
            raise ValueError('英文分數有錯')

    def total(self):
        return self.__chi + self.__eng