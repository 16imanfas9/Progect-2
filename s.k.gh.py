import random
print('game rock,paper,scissor:\nrock & paper=>paper win.\npaper & scissor=>scissor win.\nscissor & rock=>rock win!!')
emtiaz=0
while True:
    print('1.rock\n2.paper\n3.scissor')
    user_action=int(input('enter one choice:'))
    if user_action>3 or user_action<1:
        print('entered is no cerdit')
        user_action=int(input('enter one number:'))
    if user_action==1:
        user_action_name='rock'
    elif user_action==2:
        user_action_name='paper'
    else:
        user_action_name='scissor'
    print('user entkhab:',user_action_name)
    computer_action=random.randint(1,3)
    if computer_action==1:
        computer_action_name='rock'
    elif computer_action==2:
        computer_action_name='paper'
    else:
        computer_action_name='scissor'
    print('computer chice is:',computer_action_name)
    if ((user_action==1 and computer_action==3)or(user_action==2 and computer_action==1)or(user_action==3 and computer_action==2)):
        print('you win.congradualat!!')
        emtiaz+=1   
        print('emtiaz:',emtiaz)
    elif user_action==computer_action:
        print(f'both player select{user_action}itis tie.')
    else:
        print('computer win.you lose.iam sory for you!!!')
        emtiaz-=1
        print('emtiaz:',emtiaz)
    print('do you want to play again(y/n)?')
    ans=input('(y/n)')
    if ans!='y':
        break