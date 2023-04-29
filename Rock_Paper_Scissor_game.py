import random
s=input('Entre your name ')
'rules for this game is as follows'
print('Rock beats Scissor')
print('Paper beats Rock')
print('Scissor beats Paper')
print('You have to take decision in title case word')
ls=random.choice(['Rock','Paper','Scissor'])
s=input('entre your decision: ').title()
if s=='Rock' and ls=='Scissor' or s=='Paper' and ls=='Rock' or s=='Scissor' and ls=='Paper':
    print('user win')
    print('you decision is',s)
    print('computer decision is',ls)
elif s==ls:
    print('Tie game')
    print('you decision is',s)
    print('computer decision is',ls)
else:
    print('computer win')
    print('you decision is',s)
    print('computer decision is',ls)
while True:   
    a=input('entre 1 for restart the game and 0 for exit the game',)
    while a:
        ls=random.choice(['Rock','Paper','Scissor'])
        s=input('entre your decision: ').title()
        if s=='Rock' and ls=='Scissor' or s=='Paper' and ls=='Rock' or s=='Scissor' and ls=='Paper':
            print('user win')
            print('you decision is',s)
            print('computer decision is',ls)
        elif s==ls:
            print('Tie game')
            print('you decision is',s)
            print('computer decision is',ls)    
        else:
            print('computer win')
            print('you decision is',s)
            print('computer decision is',ls)
            




