def compute_score(*score):
    if len(score) >= 5:
        score = sorted([i for i in score])
        return f'{(sum(score)-score[0])/(len(score)-1):.1f}'
    elif 0 < len(score) < 5:
        return f'{sum(score)/len(score):.1f}'
    else:
        return f'0.0'



print(compute_score(70, 80, 50, 45, 90 ))
print(compute_score(75, 35, 90, 60 ))
print(compute_score())
