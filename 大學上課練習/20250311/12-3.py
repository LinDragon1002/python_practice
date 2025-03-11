def compute_socres(scores):
    temp = {'A+':95,'A':90,'B+':85,'B':80,'C':70,'D':60,'E':30}
    avg = sum([temp[s] for s in scores]) / len(scores)
    if avg >= 90:
        return f'平均分數 = {avg:.1f}\n等級 = A'
    elif avg >= 80:
        return f'平均分數 = {avg:.1f}\n等級 = B'
    elif avg >= 70:
        return f'平均分數 = {avg:.1f}\n等級 = C'
    elif avg >= 60:
        return f'平均分數 = {avg:.1f}\n等級 = D'
    else:
        return f'平均分數 = {avg:.1f}\n等級 = E'

print(compute_socres(['A+', 'A', 'A+', 'B+']))
print(compute_socres(['B', 'C', 'B', 'A', 'A']))
print(compute_socres(['C', 'B']))
print(compute_socres(['C', 'C', 'C', 'D', 'C']))
print(compute_socres(['C', 'E', 'D', 'D', 'E']))