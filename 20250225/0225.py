def compute_salary(hour:float) -> float:
    """計算薪水

    Args:
        hour (int): 工作時數

    Returns:
        int: 計算出的薪水

    Raises:
        ValueError: 參數值為負數
        TypeError: 參數不是int
    """
    if hour < 0:
        raise ValueError('參數值為負數')
    if not isinstance(hour, (int,float)):
        raise TypeError('參數不是int或float')

    total = int(220 * hour)
    return total

print(compute_salary(10))

# ------------------------------------------------------------------

def ispass(stu,*score , gender='M'):
    """判斷是否及格

    Args:
        stu (str): 學生姓名
        *score (int): 成績

    Returns:
        str: 及格與否
    """
    if stu == "A" :
        return len(score)>=3 and max(score)>=70
    else:
        return len(score)>=2 and max(score)>=60


print(ispass("A", 70, 80, 90, gender='M'))
print(ispass("B", 70, 80))