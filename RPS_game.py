from random import randint
exit = 1
while exit != '0':

    R_P_S = 0
    comp_choice = randint(0, 2)

    ls = ['R','P','S']
    computer = ls.pop(comp_choice)
    print(computer)
    print((comp_choice))

    usr_input = input('\nlet\'s play (R)ock (P)aper (S)cissors')
    if usr_input == 'R':
        R_P_S = 0
    elif usr_input == 'P':
        R_P_S = 1
    elif usr_input == 'S':
        R_P_S = 2
    else:
        pass

    if R_P_S == 0:
        if comp_choice == 1:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('You Lose :(')
        elif comp_choice == 0:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('Draw')
        else:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('You WIN ! :)')

    elif R_P_S == 1:
        if comp_choice == 2:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('You Lose :(')
        elif comp_choice == 1:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('Draw')
        else:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('You WIN ! :)')

    elif R_P_S == 2:
        if comp_choice == 0:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('You Lose :(')
        elif comp_choice == 2:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('Draw')
        else:
            print('your choice:', usr_input)
            print('computers choice:', computer)
            print('You WIN ! :)')
    else:
        pass
    a = input('continue - any key, exit: 0')
    exit = a