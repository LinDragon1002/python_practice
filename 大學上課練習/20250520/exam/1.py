#=========================    
# 類別, 寫下你的程式
#=========================   
class Score:
    def __init__(self, name,scores):
        self.name = name
        self.scores = scores
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def scores(self):
        return self.__scores
    @scores.setter
    def scores(self,scores):
        self.__scores = scores

    def average(self):
        if len(self.scores) >= 3:
            temp = sorted(self.scores,reverse=True)
            return round(sum(temp[0:3]) / 3,1)
        else:
            return round(sum(self.scores) / len(self.scores),1)
    def rank(self):
        if self.average() >= 80:
            return "A"
        elif self.average() >= 60:
            return "B"
        else:
            return "C"
#=========================    
# 主程式, 已完成, 勿改
#=========================
data = []
data.append(Score('王小明', [50, 90, 65, 45, 70, 68]))
data.append(Score('陳小華', [90, 86, 89, 91, 92, 79]))
data.append(Score('張小文', [84, 72]))
data.append(Score('蔡小梅', [70, 98, 95]))
data.append(Score('周小蓉', [45, 55, 54, 66, 76, 68, 90, 81]))
data.append(Score('黃小智', [56, 62, 77, 56, 6, 80]))

for d in data:
    print(f'姓名:{d.name}, 平均成績:{d.average()}, 等級:{d.rank()}')  


#=========================
# 參考解答
#=========================
'''
姓名:王小明, 平均成績:76.0, 等級:B
姓名:陳小華, 平均成績:91.0, 等級:A
姓名:張小文, 平均成績:78.0, 等級:B
姓名:蔡小梅, 平均成績:87.7, 等級:A
姓名:周小蓉, 平均成績:82.3, 等級:A
姓名:黃小智, 平均成績:73.0, 等級:B
'''