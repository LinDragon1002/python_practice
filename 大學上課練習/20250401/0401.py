# 函式
def total(chi,eng):
    tot = chi + eng
    return tot

# 類別
class Score:
    def __init__(self,chi,eng):
        self.chi = chi
        self.eng = eng
    # 方法(函式)
    def total(self):
        tot = self.chi + self.eng
        return tot

# 從Score類別生成一個物件s
s = Score(90,80)

# 設定s的屬性
# s.chi = 90
# s.eng = 80

# 呼叫s的方法
print(s.total())