with open ('titanic.csv', 'r')as infile:
    data = infile.readlines()
    data=[d.strip() for d in data]

    alive = []
    dead = []

    for i in data:
        _,_,result,_,_,_,age,*_ = i.split(',')

        if result == '1':
            alive.append(float(age))
        elif result == '0':
            dead.append(float(age))


    print(f'alive:{sum(alive)/len(alive):.2f}\ndead:{sum(dead)/len(dead):.2f}')