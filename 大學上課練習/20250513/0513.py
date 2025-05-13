# 初值
rank = 'A'
overhours = 5
# 判斷
if rank == 'A':
    base = 50000
elif rank == 'B':
    base = 40000
else:
    base = 30000
# 計算
total = base + 250 * overhours
# print(total)

# ----------------------------------------------

def regular_salary(rank,overhours=0):
    if rank == 'A':
        base = 50000
    elif rank == 'B':
        base = 40000
    else:
        base = 30000
    return base + 250 * overhours
def pattime_salary(hours):
    return 200 * hours

# ---------------------------------------------
# 靜態方法，在記憶體只存一份
class Employee:
    @staticmethod
    def regular_salary(rank,overhours=0):
        if rank == 'A':
            base = 50000
        elif rank == 'B':
            base = 40000
        else:
            base = 30000
        return base + 250 * overhours
    @staticmethod
    def pattime_salary(hours):
        return 200 * hours

# 用類別名稱.靜態方法名稱()，呼叫靜態方法
# print(Employee.regular_salary('A',5))
# print(Employee.pattime_salary(5))

# ---------------------------------------------
# 廣域變數(不推薦)
hourly_wage = 250
class Employee1:
    @staticmethod
    def regular_salary(rank,overhours=0):
        if rank == 'A':
            base = 50000
        elif rank == 'B':
            base = 40000
        else:
            base = 30000
        return base + hourly_wage * overhours
    @staticmethod
    def pattime_salary(hours):
        return hourly_wage * hours

# 靜態方法可取用方法內的變數或是廣域變數
# print(Employee1.regular_salary('A',5))
# print(Employee1.pattime_salary(5))

# ---------------------------------------------
# 類別變數
class Employee2:
    # 類別變數
    hourly_wage = 250
    @classmethod
    def regular_salary(cls,rank,overhours=0):
        if rank == 'A':
            base = 50000
        elif rank == 'B':
            base = 40000
        else:
            base = 30000
        return base + cls.hourly_wage * overhours # cls.代表類別變數
    @classmethod
    def pattime_salary(cls,hours):
        return cls.hourly_wage * hours
# 取出公開的類別變數
# print(Employee2.hourly_wage)
# print(Employee2.regular_salary('A',5))
# print(Employee2.pattime_salary(5))

# -------------------------------------------
# 私用的類別變數
class Employee3:
    # 類別變數
    __hourly_wage = 250
    __tax_rate = 0.08
    @classmethod
    def regular_salary(cls,rank,overhours=0):
        if rank == 'A':
            base = 50000
        elif rank == 'B':
            base = 40000
        else:
            base = 30000
        return base + cls.__hourly_wage * overhours # cls.代表類別變數
    @classmethod
    def pattime_salary(cls,hours):
        return cls.__hourly_wage * hours
    @classmethod
    def regular_tax(cls,rank,overhours=0):
        return cls.regular_salary(rank,overhours) * cls.__tax_rate
    @classmethod
    def pattime_tax(cls,hours):
        return cls.pattime_salary(hours) * cls.__tax_rate

print(Employee3.regular_salary('A',5))
print(Employee3.regular_salary('B',15))
print(Employee3.regular_salary('C'))

print(Employee3.pattime_salary(45))
print(Employee3.pattime_salary(55))
print(Employee3.pattime_salary(30))

print(Employee3.regular_tax('A',5))
print(Employee3.regular_tax('B',15))
print(Employee3.regular_tax('C'))

print(Employee3.pattime_tax(45))
print(Employee3.pattime_tax(55))
print(Employee3.pattime_tax(30))