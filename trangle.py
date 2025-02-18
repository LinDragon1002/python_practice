tall = int(input())
tall1 = tall
number = 1
many = []
for i in range(1,tall+1):
    many.append(i)
    for j in range(tall1,0,-1):
        print("_",end="")
    for j in many:
        print(j,end="")
    for j in range(len(many)-1,0,-1):
        print(j,end="")
    for j in range(tall1,0,-1):
        print("_",end="")
    tall1 -= 1
    print()