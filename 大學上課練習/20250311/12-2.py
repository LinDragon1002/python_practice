def compute_socres(scores):
    scores.remove(min(scores))
    avg = sum(scores) / len(scores)
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

print(compute_socres([60, 75, 80, 55, 90]))
print(compute_socres([90, 85, 95, 100]))
print(compute_socres([40, 55, 65, 50, 60, 45, 40]))
print(compute_socres([80, 75, 85, 95]))
print(compute_socres([65, 70, 60, 75, 50]))