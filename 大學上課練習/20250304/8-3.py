def compute_score(reading,writing,*vocabulary):
    if reading < 60 or writing < 60:
        return False
    if len(vocabulary) < 3:
        return False
    cnt = 0
    for v in vocabulary:
        if v < 60:
            cnt += 1
        if cnt >= 2:
            return False
    return True

print(compute_score(60, 55, 50, 78, 65))
print(compute_score(100, 90, 70, 80))
print(compute_score(65, 75, 90, 95, 60, 40))
print(compute_score(80, 65, 50, 75, 70, 80))