def distance():
    st1,st2 = input(),input()
    st1 = [0 if i in st2 else i for i in st1]
    temp = True
    while temp:
        for i in range(len(st1)):
            if st1[i].isdigit() and st1[i+1].islower():
                
    return st1
print(distance())