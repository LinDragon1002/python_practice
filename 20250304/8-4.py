def compute_score(reading,writing,*vocabulary):
    ans = 0
    if reading >= 70:
        ans += 1
    if writing >= 70:
        ans += 1
    for v in vocabulary:
        if v >= 70:
            ans += 1
    return ans >= 3

print(compute_score(70, 55, 50, 78, 75))
print(compute_score(100, 90, 70, 80))
print(compute_score(65, 75, 90, 65, 60, 40))
print(compute_score(50, 65, 50, 75, 70, 60))