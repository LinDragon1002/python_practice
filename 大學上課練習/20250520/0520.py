def taxi_day(meter):
    if meter <= 1250:
        return 85
    else:
        return 85 + (meter-1250) // 200 * 5
def taxi_night(meter):
    if meter <= 1250:
        return 105
    else:
        return 105 + (meter-1250) // 200 * 5

# 傳遞函式
# def taxi(meter,func=taxi_day):
#     return func(meter)

# 靜態類別
'''
|---------------------------------|
|            Taxi_fee             |
|---------------------------------|
|---------------------------------|
|<<static>> + day(meter:int):int  |
|<<static>> + night(meter:int):int|
|---------------------------------|
'''
class Taxi_fee:
    @staticmethod
    def day(meter):
        if meter <= 1250:
            return 85
        else:
            return 85 + (meter-1250) // 200 * 5
    @staticmethod
    def night(meter):
        if meter <= 1250:
            return 105
        else:
            return 105 + (meter-1250) // 200 * 5

def taxi(meter,func=Taxi_fee.day):
    return func(meter)

# 類別方法
'''
|----------------------------------|
|           Taxi_fee2              |
|----------------------------------|
|<<class>> - day_base: int         |
|<<class>> - night_base: int       |
|<<class>> - extra:int             |
|<<class>> - holiday_base:int      |
|----------------------------------|
|<<class>> + day(meter:int):int    |
|<<class>> + night(meter:int):int  |
|<<class>> + holiday(meter:int):int|
|----------------------------------|
'''

class Taxi_fee2:
    # 類別變數
    __day_base = 85
    __night_base = 105
    __extra = 5
    __holiday_base = 30

    @classmethod
    def day(cls,meter):
        if meter <= 1250:
            return cls.__day_base
        else:
            return cls.__day_base + (meter-1250) // 200 * cls.__extra
    @classmethod
    def night(cls,meter):
        if meter <= 1250:
            return cls.__night_base
        else:
            return cls.__night_base + (meter-1250) // 200 * cls.__extra
    @classmethod
    def holiday(cls,meter):
        return cls.night(meter) + cls.__holiday_base

# print(taxi(650))
# print(taxi(1650))
# print(taxi(2650))

# print(taxi(650,Taxi_fee.night))
# print(taxi(1650,Taxi_fee.night))
# print(taxi(2650,Taxi_fee.night))

# 計數器
# 廣域變數
cnt = 0
def counter():
    global cnt
    cnt += 1
    print(cnt)

def my_counter():
    # nonlocal變數
    cnt = 0
    def counter():
        nonlocal cnt
        cnt += 1
        print(cnt)

    return counter
# counter = my_counter()
# counter()
# counter()
# counter()

# 裝飾器
def my_decorator(func):
    def wrapper(*args,**kwargs):
        name = func(*args,**kwargs)
        return name.upper()
    return wrapper
@my_decorator
def myname(name):
    return name
print(myname('DragonCorn'))