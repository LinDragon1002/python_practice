def compute_commission(total,rank):
    if 65 <= ord(rank) <= 75:
        total = int(total * 0.14)
    elif 76 <= ord(rank) <= 82:
        total = int(total * 0.12)
    elif 83 <= ord(rank) <= 90:
        total = int(total * 0.11)
    return f'{total:,}'

total = 62375
rank = "T"
print(compute_commission(total,rank))
