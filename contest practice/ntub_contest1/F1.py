def rank(score,practice1=0,practice2=0):
    total = sum(score)/len(score) * 0.4 + practice1 * 0.3 + practice2 * 0.3
    if total >= 90:
        return "A"
    elif 80 <= total < 90:
        return "B"
    elif 70 <= total < 80:
        return "C"
    elif 60 <= total < 70:
        return "D"
    else:
        return "E"


allscore = [int(i) for i in input().split(' ')]
print(rank(allscore[:-2], allscore[-2], allscore[-1]))
