Adult = 20
Teenager = 13
Child = 1
Infant = 0


Age = float(input('Enter an age: '))

if Age >= Adult:
    print('Adult')
else:
    if Age >=Teenager:
        print('Teenager')
    else:
        if Age >= Child:
            print('Child')
        else:
            print('Infant')

