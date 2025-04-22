class Score:
    def __init__(self,chi,eng,mat):
        self.chi = chi # 這裡會呼叫chi的setter
        self.eng = eng
        self.mat = mat

    @property # 這是屬性裝飾器，讓我們可以用get_chi()來取得__chi的值
    def chi(self):
        return f'國文:{self.__chi}'
    @property
    def eng(self):
        return f'英文:{self.__eng}'
    @property
    def mat(self):
        return f'數學:{self.__mat}'

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

    @mat.setter
    def mat(self,mat):
        if 0 <= mat <= 100:
            self.__mat = mat
        else:
            raise ValueError('數學分數有錯')

    def total(self):
        return f'總分:{self.__chi + self.__eng + self.__mat}'

s1 = Score(70,80,90)
s2 = Score(65,82,73)

print(s1.chi,s1.eng,s1.mat,s1.total(),sep=',')
print(s2.chi,s2.eng,s2.mat,s2.total(),sep=',')
