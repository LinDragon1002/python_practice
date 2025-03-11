def compute_score(*score):
    if not score:
        return f'0.0'
    return f'{sum(score) / len(score):.1f}'



print(compute_score(90,80,70))
print(compute_score( 95, 80, 70, 90, 65, 70 ))
print(compute_score())