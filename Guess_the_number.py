import random
#here s is number of attempt
print('''You have to guess the number between 1 to 15
you have 10 attempt for the beignner level''')
s=10
val=random.randint(1,15)
score=10
while s>0:
    number=int(input('Guess the number: '))
    if number<val:
        print('your number is small')
        score-=1
        s=s-1
        print('your reamaining attempt is: ',s)
    elif number>val:
        print('your number is large')
        score-=1
        s=s-1
        print('your reamaining attempt is: ',s)
    elif number==val:
        print('correct guess')
        break
print('your score is',score)
if score==0:
    print('loser')
if score>0:
    print('you have reached level 1')
    print('you have only 5 attempt to guess the number')
    #here s is number of attempt
    s=5
    val=random.randint(1,15)
    score=5
    while s!=0:
        number=int(input('Guess the number: '))
        if number<val:
            print('your number is small')
            score-=1
            s=s-1
            print('your reamaining attempt is: ',s)
        elif number>val:
            print('your number is large')
            score-=1
            s=s-1
            print('your reamaining attempt is: ',s)
        elif number==val:
            print('correct guess')
            break
    print('your score is',score)
    if score==0:
        print('loser')
    if score>0:
        print('you have reached highest level')
        print('you have only 3 attempt to guess the number')
        #here s is number of attempt
        s=3
        val=random.randint(1,15)
        score=3
        while s!=0:
            number=int(input('Guess the number: '))
            if number<val:
                print('your number is small')
                score-=1
                s=s-1
                print('your reamaining attempt is: ',s)
            elif number>val:
                print('your number is large')
                score-=1
                s=s-1
                print('your reamaining attempt is: ',s)
            elif number==val:
                print('correct guess')
                break
        print('your score is',score)
        if score==0:
            print('Loser')
        
        





