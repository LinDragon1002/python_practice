class Student:
    def __init__(self,no,name):
        self.no = no
        self.name = name
    def department(self):
        if str(self.no)[4] == "6":
            return "資管"
        else:
            return "其他"

s1 = Student(11256001,"王小明")
s2 = Student(11257002,"陳小華")
print(s1.department())
print(s2.department())
